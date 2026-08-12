# Week 21 AI Semantic Search Assistant  
  
A compact Flask semantic search assistant that compares TF-IDF, Cosine, Euclidean, and embedding-based retrieval on the same   document corpus.  
  
## Overview  
  
This product accepts natural-language queries and returns four ranked Top-5 result lists:  
- TF-IDF search  
- Cosine similarity search  
- Euclidean distance search  
- Embedding search  
  
The UI displays all four rankings side by side so users can compare result stability and ranking differences.  
  
## Features  
  
- Natural-language query input with prompt injection protection  
- TF-IDF Top-5 ranking  
- Cosine Top-5 ranking  
- Euclidean Top-5 ranking  
- Embedding Top-5 ranking  
- Side-by-side ranking comparison for algorithm analysis  
- Multilingual query support for Chinese, Spanish, French, English, and other Unicode text  
- Prompt filter that rejects control characters, zero-width characters, direct bypass phrases, and suspicious instruction-target   combinations  
- Machine-readable results for 20 queries across TF-IDF, Cosine, Euclidean, and Embedding  
- Linux-compatible CI with pinned dependencies and full pytest execution  
  
## How the algorithms compare  
  
- Cosine similarity returns higher values for more similar vectors.  
- Euclidean distance returns lower distance values for closer vectors.  
- TF-IDF ranks by term relevance and inverse document frequency.  
- Embedding search ranks by semantic similarity from sentence embeddings.  
- Differences between Cosine and Euclidean often reflect normalization and ranking direction.  
  
## Repository structure  
  
.  
├── .github/  
│   └── workflows/test.yml  
├── Week21_Engineering/  
│   ├── Implementation1/Similarity_Engine/similarity.py  
│   ├── Implementation2/TFIDF_Retrieval/tfidf_search.py  
│   ├── Implementation3/Embedding_Similarity/embedding_similarity.py  
│   ├── Implementation4/Vector_Search/vector_search.py  
│   ├── Implementation5/Embedding_Search/embedding_search.py  
│   ├── Implementation6/Gradient_Descent/gradient_descent_demo.py  
│   ├── Implementation7/Embedding_Failure_Analysis/embedding_failure_analysis.py  
│   └── shared/shared.py  
├── app.py  
├── dataset.json  
├── prompt_filter.py  
├── record.py  
├── requirements.txt  
├── report/  
│   ├── architecture.md  
│   ├── model_analysis.md  
│   ├── project reflection.md  
│   ├── prompt filter result.md  
│   ├── security_analysis.md  
│   ├── security_report.md  
│   ├── testing_results.md  
│   └── user_manual.md  
├── static/  
├── templates/  
├── tests/  
│   ├── fixtures/  
│   │   ├── prompt_filter_cases.json  
│   │   └── sample_queries.json  
│   ├── results_20_queries.json  
│   ├── test_dataset_validation.py  
│   ├── test_euclidean_vs_cosine.py  
│   ├── test_failure_cases.py  
│   ├── test_multilingual_input.py  
│   ├── test_product_flow.py  
│   ├── test_prompt_filter.py  
│   └── test_20_queries.py  
├── timeline.json  
└── bin/  
    ├── development_notes.md  
  
## Python and CI  
  
- Validated on Python 3.12 and Ubuntu Linux  
- CI runs `pip install -r requirements.txt` and `python -m pytest tests -q`  
  
## Notes  
  
- The prompt filter is intentionally permissive for Unicode input and only rejects known injection patterns, control characters,   and zero-width hidden text.  
- The repository includes a machine-readable 20-query results file at `tests/results_20_queries.json` for reproducible validation.  
  