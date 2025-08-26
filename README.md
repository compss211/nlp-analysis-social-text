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
│   └── nlp_analysis.ipynb     
└── output/
    └── (your output files will go here)
```

### Setup Instructions (Local)

1. **Clone this repository** from GitHub Classroom

2. **Create a conda environment** (recommended):
   ```bash
   conda create -n nlp-hw5 python=3.9
   conda activate nlp-hw5
   ```
   
   Note: If you don't have conda installed, you can get it from [Anaconda](https://www.anaconda.com/products/individual) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (lighter weight).

3. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Open the notebook**: 
   - **Jupyter**: `jupyter notebook notebooks/nlp_analysis.ipynb`
   - **VSCode**: Open the notebook file 

---

## Assignment: Basic NLP Analysis

This assignment provides a structured approach to analyzing social discourse patterns in Reddit's r/ChangeMyView community using fundamental NLP techniques.

### Required Tasks:
1. **Data Loading & Basic Exploration**
   - Successfully load both datasets (posts and comments)
   - Perform basic data exploration (shape, columns, missing values)
   - Create simple statistics (average post length, comment counts)
   - Visualize basic distributions (post scores, comment lengths)

2. **Text Preprocessing**
   - Clean text data (remove special characters, lowercase)
   - Tokenize posts and comments
   - Remove stopwords using NLTK
   - Create and compare word frequency distributions

3. **Comparative Analysis**
   - Find the top 20 most common words in posts vs comments
   - Create word clouds for posts and comments separately
   - Calculate basic text statistics (average word length, vocabulary size)
   - Identify unique words that appear only in posts or only in comments

4. **Sentiment Analysis**
   - Apply a pre-built sentiment analyzer (VADER or TextBlob)
   - Compare sentiment distributions between posts and comments
   - Find the most positive and negative posts/comments
   - Create visualizations of sentiment patterns

5. **Interpretation**
   - Write a 2-paragraph summary of your findings
   - Discuss one interesting pattern you discovered
   - Suggest one way these findings could be useful in a social science setting

### Expected Deliverables:
- Completed notebook with all code cells executed
- At least 4 visualizations
- Written interpretation of findings
- Documentation of any challenges faced

### Stretch Goals (Optional)

For students who complete the basic analysis and want additional challenges:

1. **Advanced Text Analysis**
   - Link posts to their comments using ID columns
   - Implement TF-IDF to find distinctive vocabulary between posts and comments
   - Apply named entity recognition to identify key topics

2. **Conversation Dynamics**
   - Calculate semantic similarity between posts and their comments
   - Analyze response patterns (agreement vs disagreement language)
   - Identify high-engagement conversation characteristics

3. **Word Embeddings**
   - Load and apply pre-trained word embeddings (GloVe or Word2Vec)
   - Calculate semantic distances between key concepts
   - Visualize word relationships in semantic space

4. **Machine Learning Applications**
   - Build a classifier to predict comment engagement levels
   - Implement topic modeling (LDA) to discover conversation themes
   - Explore what linguistic features correlate with successful persuasion

---

## Optional: Advanced Example Approach

### Exploring Modern NLP with RAG and LLMs

In the `example_approach/` folder, you'll find an example of an approach to analyzing CMV conversations using Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs). This example is **entirely optional** and provided for inspiration only.

**What the example demonstrates:**
- **Data Collection via API**: Using PRAW (Python Reddit API Wrapper) to collect fresh CMV data with delta tracking
- **Delta Analysis**: Identifying which comments successfully changed views (marked by delta awards)
- **RAG Implementation**: Using TF-IDF retrieval to find relevant conversation snippets
- **LLM Analysis**: Employing Qwen 2.5 to analyze persuasion patterns and rhetorical strategies
- **Structured Output**: Generating JSON-formatted insights about what makes arguments persuasive

**Key Concepts You Could Adapt (without LLMs):**
- **Success Metrics**: Analyzing differences between comments that changed views vs those that didn't
- **Conversation Threading**: Following argument chains from initial post to resolution
- **Persuasion Patterns**: Identifying linguistic features of successful arguments
- **Rhetorical Analysis**: Examining ethos, pathos, logos in argumentation

**Important Notes:**
- This approach requires additional dependencies (PRAW, transformers, torch)
- LLM inference benefits greatly from GPU access (Google Colab)
- The focus includes traditional NLP and prompt engineering
- You can extract ideas without implementing the full stack

**If You're Interested:**
- Advanced pathway students might incorporate LLM-based analysis
- You could use simpler methods to explore similar research questions
- Consider the delta concept in r/changemyview: What language patterns correlate with view changes?
- Think about how traditional NLP methods could answer similar questions

Remember: This is one possible approach among many. Your creativity in applying NLP techniques to understand online discourse is what matters most.

---

## Tips for Success

1. **Start with exploration**: Understand your data before diving into analysis
2. **Document as you go**: Explain your thinking and choices
3. **Visualize findings**: Good visualizations tell the story better than numbers
4. **Think critically**: What do these patterns really mean for online discourse?

---

## Common Issues and Solutions

- **Word embeddings loading**: The first time loading GloVe embeddings may take a few minutes and ~200MB download
- **Dataset linking errors**: Ensure you're using the correct ID columns (`posts['id']` and `comments['link_id']`)
- **Memory issues with large datasets**: Work with samples if needed, or use the provided subsets
- **Missing NLTK data**: The notebooks will download required NLTK resources automatically  
- **Import errors**: Make sure you've installed all packages from requirements.txt, including `gensim`
- **Empty conversations**: Some posts may have no comments in the dataset - handle these cases gracefully

---

## Academic Integrity

- You may use AI tools (ChatGPT, Copilot, etc.) to help with coding, but you must:
  - Document any AI assistance in code comments
  - Understand and be able to explain all code you submit
  - Write your own interpretation and analysis
- Collaboration is encouraged for understanding concepts, but each student must submit their own work
- Clearly indicate which pathway you chose at the top of your notebook

---

## Submission

2. **Complete all required tasks** for your chosen pathway
3. **Push to GitHub Classroom** with:
   - Completed notebook
   - Any additional output files in the `output/` folder
   - Clear indication of which pathway you followed

---

## Additional Resources

### General NLP:
- [NLTK Documentation](https://www.nltk.org/)
- [Scikit-learn Text Feature Extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)
- [Pandas DataFrame Merging](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html)

### Word Embeddings:
- [Gensim Word2Vec Tutorial](https://radimrehurek.com/gensim/models/word2vec.html)
- [Word Embeddings Guide](https://machinelearningmastery.com/what-are-word-embeddings/)
- [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/projects/glove/)

### Advanced Techniques:
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [spaCy Documentation](https://spacy.io/)
- [Multi-document NLP Techniques](https://www.aclweb.org/anthology/)

### Online Discourse Research:
- [CMV Dataset Paper](https://arxiv.org/abs/1602.01103)
- [Argument Mining Survey](https://www.aclweb.org/anthology/J17-3001/)
- [Online Deliberation Theory](https://www.annualreviews.org/doi/10.1146/annurev-polisci-032317-092722)
