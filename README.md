# Week21_AI_Semantic_Search_Assistant

This project is a compact Flask-based semantic search assistant that compares TF-IDF, dense vector similarity, and a simple gradient descent demo in one runnable package.

## Overview

The application lets users submit a natural-language query and view multiple retrieval strategies side by side. It is intended as an educational product that shows how keyword-based search and embedding-style search behave on the same document corpus.

## Features

- Query input with prompt filtering
- TF-IDF ranking results
- Cosine similarity comparison
- Embedding-style retrieval results
- Simple gradient descent demo showing how it works, including loss, w and b.
- Failure analysis for ambiguous or out-of-domain queries
- Embedding search similarity

## Project Structure

Copied from PowerShell (Latest version, really!!!):
```text
D:.
├── README.md
├── Week21_Engineering
│   ├── Implementation1
│   │   └── Similarity_Engine
│   │       └── similarity.py
│   ├── Implementation2
│   │   └── TFIDF_Retrieval
│   │       └── tfidf_search.py
│   ├── Implementation3
│   │   └── Embedding_Similarity
│   │       └── embedding_similarity.py
│   ├── Implementation4
│   │   └── Vector_Search
│   │       └── vector_search.py
│   ├── Implementation5
│   │   └── Embedding_Search
│   │       └── embedding_search.py
│   ├── Implementation6
│   │   └── Gradient_Descent
│   │       └── gradient_descent_demo.py
│   ├── Implementation7
│   │   └── Embedding_Failure_Analysis
│   │       └── embedding_failure_analysis.py
│   └── shared
│       └── shared.py
├── __init__.py
├── app.py
├── bin
│   ├── fix error(just for checking and show how it work).py
│   └── my work.md
├── dataset.json
├── examples
│   ├── example 1.png
│   ├── example 2.png
│   ├── example 3.png
│   ├── example 4.png
│   └── example 5.png
├── prompt_filter.py
├── record.py
├── report
│   ├── project reflection.md
│   ├── prompt filter result.md
│   ├── proof 1.png
│   ├── proof 2.png
│   └── security_report.md
├── requirements.txt
├── static
│   ├── app.css
│   └── app.js
├── templates
│   └── index.html
├── tests
│   ├── fixtures
│   │   └── sample_queries.json
│   ├── test_product_flow.py
│   └── test_search.py
├── timeline.json
└── unfilted_test.py
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```

Then open http://localhost:5000 and enter a query such as "machine learning", "semantic search", or "bank".

## Verification

The repository now includes:

- regression tests in the tests folder
- Included many testing result and report in report/ , such as project reflection, prompt filter result and security_report.

## Notes

The current implementation uses a deterministic fallback embedding strategy when a pretrained sentence-transformer model is unavailable, which makes the project reproducible in a classroom environment.

## Prompt Filtering

Added strong prompt filtering including hidden symbols, random symbols, and prompt injection blocking, with a comparison of system performance before and after filtering.  
The results improved from 50% to 100% (prompt_filter 100%, filtered_test 50%, see proof 1 and proof 2 which contain 4 harmful prompts and 4 safe prompts for testing).

## Testing Results

There are 5 images showing the results, named example 1, 2, 3, 4, and 5.

## Embedding backend:
There are two models:
- sentence-transformers/all-MiniLM-L6-v2
- deterministic fallback

## CI
Action: Enabled  
Workflow: .github/workflows/test.yml  
Actions: pip install -r requirements.txt + pytest  