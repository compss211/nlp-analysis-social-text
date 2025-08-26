#!/usr/bin/env python3
"""
cmv_scrape.py — Minimal PRAW pipeline for r/changemyview

What it does (kept simple):
1) Build a submissions CSV from /r/changemyview top posts
2) Build a comments CSV with a delta_awarded flag for parent comments that OP awarded

Best practices folded in:
- Auth via environment variables (optionally .env)
- Conservative defaults + simple params
- Robust attribute access (avoid crashes on missing fields)
- Progress bars and small, readable helpers
- Consistent, tidy CSV schemas
"""

import os
import argparse
from typing import List, Set, Optional

import pandas as pd
from tqdm import tqdm

try:
    from dotenv import load_dotenv  # optional
    load_dotenv()
except Exception:
    pass

import praw


# -------------------------
# Auth
# -------------------------

def get_reddit() -> praw.Reddit:
    """Create a Reddit client from environment variables.

    Set before running (e.g. in your shell or .env):
        export REDDIT_CLIENT_ID="..."
        export REDDIT_CLIENT_SECRET="..."
        export REDDIT_USER_AGENT="changemyview-data-lab/0.1 by YOUR_NAME"
    """
    cid = os.getenv('REDDIT_CLIENT_ID')
    csec = os.getenv('REDDIT_CLIENT_SECRET')
    ua = os.getenv('REDDIT_USER_AGENT', 'changemyview-data-lab/0.1')

    if not cid or not csec:
        raise RuntimeError('Missing REDDIT_CLIENT_ID or REDDIT_CLIENT_SECRET')

    return praw.Reddit(
        client_id=cid,
        client_secret=csec,
        user_agent=ua,
        check_for_async=False,
    )


# -------------------------
# Utilities
# -------------------------

def flair_is_delta_from_op(flair: Optional[str]) -> bool:
    """Heuristic: submissions whose flair text mentions a delta from OP."""
    if not flair:
        return False
    t = str(flair).strip().lower()
    return ('delta' in t) and ('from op' in t)


# A small but practical list of delta cues (example .py + a couple extras)
DELTA_TOKENS: List[str] = [
    '∆', '\u2206', '!delta', 'delta awarded', 'i award you a delta',
    'i award a delta', "i'm awarding a delta", 'i am awarding a delta'
]

def has_delta(text: Optional[str]) -> bool:
    """Does the text look like an OP awarding a delta?"""
    if not text:
        return False
    t = str(text).lower()
    return any(tok in t for tok in DELTA_TOKENS)


# -------------------------
# Submissions
# -------------------------

def fetch_top_submissions(reddit: praw.Reddit, subreddit_name: str, time_filter: str, limit: int) -> pd.DataFrame:
    """Fetch top submissions and return a tidy dataframe."""
    sub = reddit.subreddit(subreddit_name)
    rows = []
    for s in tqdm(sub.top(time_filter=time_filter, limit=limit), total=limit, desc='Top submissions'):
        rows.append({
            'id': getattr(s, 'id', None),
            'title': getattr(s, 'title', '') or '',
            'author': str(getattr(s, 'author', None)) if getattr(s, 'author', None) else None,
            'permalink': f"https://reddit.com{getattr(s, 'permalink', '')}",
            'url': getattr(s, 'url', None),
            'created_utc': getattr(s, 'created_utc', None),
            'score': getattr(s, 'score', None),
            'num_comments': getattr(s, 'num_comments', None),
            'upvote_ratio': getattr(s, 'upvote_ratio', None),
            'link_flair_text': getattr(s, 'link_flair_text', None),
            'total_awards_received': getattr(s, 'total_awards_received', None),
        })
    return pd.DataFrame(rows)


def build_submissions_csv(
    reddit: praw.Reddit,
    outfile: str,
    subreddit_name: str = 'changemyview',
    time_filter: str = 'all',
    limit: int = 1000,
) -> pd.DataFrame:
    """Create a submissions CSV with a simple 'has_delta_from_op' flag from flair."""
    df = fetch_top_submissions(reddit, subreddit_name, time_filter, limit)
    if df.empty:
        Path(outfile).parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(outfile, index=False)
        print(f'Wrote 0 rows to {outfile}')
        return df

    df['has_delta_from_op'] = df['link_flair_text'].apply(flair_is_delta_from_op)
    # keep only posts with a real OP
    df = df[df['author'].notna()]

    cols = [
        'id','title','author','permalink','url','created_utc','score',
        'num_comments','upvote_ratio','link_flair_text','has_delta_from_op',
        'total_awards_received'
    ]
    out = df[cols].copy()

    Path(outfile).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(outfile, index=False)
    print(f'Wrote {len(out)} rows to {outfile}')
    return out


# -------------------------
# Comments
# -------------------------

def build_comments_csv(
    reddit: praw.Reddit,
    submissions_csv: str,
    outfile: str,
    n_submissions: int = 50,
    max_comments: int = 1000,
    replace_more_limit: int = 5,
    replace_more_threshold: int = 10,
) -> pd.DataFrame:
    """Create a comments CSV with 'delta_awarded' True for parent comments OP awarded.

    Two-pass logic per submission:
      1) Find OP delta award comments (by OP) and collect the parent comment ids.
      2) Emit all comments with a 'delta_awarded' flag if their id is in that parent set.
    """
    subs = pd.read_csv(submissions_csv)
    subs = subs[subs['author'].notna() & (subs['author'].str.lower() != '[deleted]')].copy()
    subs = subs.head(n_submissions)

    rows = []
    total = 0

    for _, srow in tqdm(subs.iterrows(), total=len(subs), desc='Scanning submissions'):
        sid = srow['id']
        op = str(srow['author'])
        subm = reddit.submission(id=sid)
        subm.comment_sort = 'top'
        subm.comments.replace_more(limit=replace_more_limit, threshold=replace_more_threshold)

        comment_list = subm.comments.list()

        # pass 1: detect which parent comment ids received a delta from OP
        awarded_parent_ids: Set[str] = set()
        for c in comment_list:
            c_body = getattr(c, 'body', '') or ''
            c_author = str(getattr(c, 'author', None)) if getattr(c, 'author', None) else None
            if (c_author == op) and has_delta(c_body):
                parent_full = getattr(c, 'parent_id', '') or ''
                if parent_full.startswith('t1_'):  # parent is a comment
                    awarded_parent_ids.add(parent_full.split('_', 1)[1])

        # pass 2: emit rows (minimal but useful schema)
        for c in comment_list:
            if total >= max_comments:
                break
            parent_full = getattr(c, 'parent_id', '') or ''
            parent_comment_id = parent_full.split('_', 1)[1] if parent_full.startswith('t1_') else None

            rows.append({
                'comment_id': getattr(c, 'id', None),
                'post_id': sid,
                'parent_comment_id': parent_comment_id,
                'score': getattr(c, 'score', None),
                'author': str(getattr(c, 'author', None)) if getattr(c, 'author', None) else None,
                'is_op': (str(getattr(c, 'author', None)) == op) if getattr(c, 'author', None) else False,
                'delta_awarded': (getattr(c, 'id', None) in awarded_parent_ids),
                'body': getattr(c, 'body', '') or '',
                'permalink': f"https://reddit.com{getattr(c, 'permalink', '')}",
                'created_utc': getattr(c, 'created_utc', None),
                'depth': getattr(c, 'depth', None),
            })
            total += 1

        if total >= max_comments:
            break

    df = pd.DataFrame(rows)
    Path(outfile).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(outfile, index=False)
    print(f'Wrote {len(df)} rows to {outfile}')
    return df


# -------------------------
# CLI
# -------------------------

def main():
    p = argparse.ArgumentParser(description='Minimal CMV scraper (submissions + comments)')
    p.add_argument('--submissions_out', default='data/submissions.csv')
    p.add_argument('--comments_out', default='data/comments.csv')
    p.add_argument('--subreddit', default='changemyview')
    p.add_argument('--time_filter', default='all', choices=['day','week','month','year','all'])
    p.add_argument('--limit', type=int, default=1000, help='Top submissions to fetch')
    p.add_argument('--n_submissions', type=int, default=100, help='How many submissions to scan for comments')
    p.add_argument('--max_comments', type=int, default=50000)
    p.add_argument('--replace_more_limit', type=int, default=0)
    p.add_argument('--replace_more_threshold', type=int, default=0)
    args = p.parse_args()

    reddit = get_reddit()

    # 1) Submissions CSV
    build_submissions_csv(
        reddit,
        outfile=args.submissions_out,
        subreddit_name=args.subreddit,
        time_filter=args.time_filter,
        limit=args.limit,
    )

    # 2) Comments CSV
    build_comments_csv(
        reddit,
        submissions_csv=args.submissions_out,
        outfile=args.comments_out,
        n_submissions=args.n_submissions,
        max_comments=args.max_comments,
        replace_more_limit=args.replace_more_limit,
        replace_more_threshold=args.replace_more_threshold,
    )


if __name__ == '__main__':
    from pathlib import Path
    main()