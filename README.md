# HW 5: NLP Analysis of Social Text 

---

## Overview

This assignment focuses on conversations in Reddit's r/ChangeMyView community. You will apply your NLP skills to analyze discourse patterns across linked posts and comments from this community.

### Learning Objectives

- Link and analyze multiple related text documents
- Compare language patterns between posts (arguments) and comments (responses)  
- Apply word embeddings to analyze social discourse dynamics
- Investigate conversation patterns and discussion quality
- Connect NLP findings to theories of online deliberation and persuasion

### Datasets

This analysis uses two linked datasets from Reddit's r/ChangeMyView community:

**Posts Dataset** (`data/changemyview_posts.csv`): 5,000 top-ranked CMV submissions
- `title`: The CMV post title (opinion to be changed)
- `selftext`: The post body/content with argument
- `score`: Reddit upvotes (engagement measure)
- `num_comments`: Number of comments (discussion level)
- `id`: Unique post identifier for linking to comments

**Comments Dataset** (`data/cmv_comments.csv`): 12,106 top-rated comments
- `body`: Comment text content
- `score`: Comment upvotes
- `link_id`: Links comment to its parent post
- Additional metadata for conversation analysis

r/ChangeMyView is a subreddit where people post views they're willing to have challenged, creating an ideal environment for studying reasoned discourse and opinion change.

### Repository Structure

```
nlp-analysis-social-text/
├── README.md                           # This file
├── requirements.txt                    # Python dependencies
├── data/
│   ├── changemyview_posts.csv         # CMV posts dataset
│   └── cmv_comments.csv               # CMV comments dataset
├── notebooks/
│   └── nlp_analysis_starter.ipynb     # HW5: Multi-document NLP analysis
└── output/
    └── (your output files will go here)
```

### Setup Instructions

1. **Clone this repository** from GitHub Classroom

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

5. **Then work on the homework**: `notebooks/nlp_analysis_starter.ipynb`

### Assignment Tasks

#### Part 1: Dataset Linking & Multi-Document Preprocessing (20 points)
- Link posts to their comments using shared ID columns
- Apply consistent preprocessing to both posts and comments
- Handle missing data and empty texts appropriately
- Document your approach to multi-document preprocessing

#### Part 2: Comparative Language Analysis (20 points)
- Compare word frequencies between posts (arguments) and comments (responses)
- Identify distinctive vocabulary for each document type
- Visualize language differences and discuss their implications
- Analyze what these patterns reveal about different communication purposes

#### Part 3: Conversation Analysis (20 points)  
- Create post-comment pairs for conversations with multiple responses
- Calculate semantic similarity between posts and their comments
- Analyze conversation dynamics and response patterns
- Identify characteristics of high-engagement discussions

#### Part 4: Word Embeddings & Social Discourse (20 points)
- Apply word embeddings techniques from the lab to analyze semantic patterns
- Create semantic axes relevant to social/political discourse
- Project key terms onto these axes to analyze discourse positioning
- Compare semantic patterns between posts and comments

#### Part 5: Social Dynamics Interpretation (20 points)
- Write a 3-4 paragraph interpretation addressing social science questions
- Connect findings to theories of online deliberation and persuasion
- Discuss what patterns reveal about productive vs. unproductive discourse
- Consider implications for designing better discussion platforms

### Deliverables

1. **Completed Lab Notebook**: `word_embeddings_lab.ipynb` with group reflections

2. **Completed HW5 Notebook**: `nlp_analysis_starter.ipynb` with:
   - All code cells executed showing multi-document analysis
   - Your interpretation and analysis in markdown cells
   - Clear documentation of your linking and preprocessing approach

3. **Multi-Document Analysis Summary** (in HW5 notebook):
   - Key findings from linking posts with comments
   - Insights about language differences between posts and responses
   - Word embeddings analysis of social discourse patterns
   - Social science interpretation connecting findings to theories of online deliberation
   - Discussion of what conversation patterns reveal about productive discourse

4. **Push to GitHub Classroom**:
   - Commit both completed notebooks
   - Include any additional output files in the `output/` folder
   - Ensure all code runs without errors

### Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Lab Completion | 10 | Completed word embeddings lab with group reflections |
| Dataset Linking | 20 | Successfully links posts with comments, handles data quality |
| Multi-Doc Analysis | 25 | Thorough comparison of posts vs comments using multiple techniques |
| Word Embeddings | 20 | Applies semantic axes to analyze social discourse patterns |
| Social Interpretation | 15 | Thoughtful connection to theories of online deliberation |
| Documentation | 10 | Clear explanations of methods and multi-document approach |

### Tips for Success

1. **Think about relationships**: Focus on how posts and comments relate to each other, not just individual documents
2. **Use the linking structure**: Take advantage of the post-comment relationships to analyze conversations
3. **Build on the lab**: Apply semantic axes and word embeddings techniques from our lab sessions
4. **Think about discourse dynamics**: Consider how initial arguments (posts) generate different types of responses (comments)
5. **Consider platform norms**: r/ChangeMyView has unique rules about respectful debate - how do these affect language patterns?
6. **Connect to social theory**: Link your computational findings to broader questions about persuasion, deliberation, and opinion change
7. **Document your linking approach**: Explain how you connected the datasets and handled any data quality issues

### Common Issues and Solutions

- **Word embeddings loading**: The first time loading GloVe embeddings may take a few minutes and ~200MB download
- **Dataset linking errors**: Ensure you're using the correct ID columns (`posts['id']` and `comments['link_id']`)
- **Memory issues with large datasets**: Work with samples if needed, or use the provided subsets
- **Missing NLTK data**: The notebooks will download required NLTK resources automatically  
- **Import errors**: Make sure you've installed all packages from requirements.txt, including `gensim`
- **Empty conversations**: Some posts may have no comments in the dataset - handle these cases gracefully

### Academic Integrity

- You may use AI tools (ChatGPT, Copilot, etc.) to help with coding, but you must:
  - Document any AI assistance in code comments
  - Understand and be able to explain all code you submit
  - Write your own interpretation and analysis
- Collaboration is encouraged for understanding concepts, but each student must submit their own work

### Submission

Submit through GitHub Classroom by pushing your completed notebook and any additional files to your repository.

### Additional Resources

- [Gensim Word2Vec Tutorial](https://radimrehurek.com/gensim/models/word2vec.html)
- [NLTK Documentation](https://www.nltk.org/)
- [Scikit-learn Text Feature Extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)
- [Pandas DataFrame Merging](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html)
- [Word Embeddings Guide](https://machinelearningmastery.com/what-are-word-embeddings/)
- [Multi-document NLP Techniques](https://www.aclweb.org/anthology/)

---

Good luck with your analysis! Remember, this is about more than running code - you're exploring how computational methods can reveal patterns in social interaction and help us understand online discourse, persuasion, and the dynamics of opinion change in digital communities.
