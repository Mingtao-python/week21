# Architecture Diagram and Module Responsibilities

## System overview

The product is a Flask web application that accepts user queries, filters them for prompt injection risks, executes four retrieval algorithms, and renders all Top-5 results in a comparison view.

## Module responsibilities

- `app.py`
  - Flask entrypoint and request handler.
  - Calls `prompt_filter.filter_prompt` before retrieval.
  - Routes queries to TF-IDF, Cosine, Euclidean, and Embedding search.
  - Renders `templates/index.html` with all algorithm outputs.

- `prompt_filter.py`
  - Normalizes and validates input text.
  - Rejects control characters, zero-width characters, direct bypass phrases, and suspicious action-target combinations.
  - Allows valid Unicode languages including Chinese, Spanish, and French.

- `record.py`
  - Records query outcomes and metadata for audit logging.

- `Week21_Engineering/Implementation1/Similarity_Engine/similarity.py`
  - Defines `cosine_similarity` and `euclidean_distance` helper functions.

- `Week21_Engineering/Implementation2/TFIDF_Retrieval/tfidf_search.py`
  - Computes TF-IDF vectors and returns top-k results by cosine relevance.

- `Week21_Engineering/Implementation3/Embedding_Similarity/embedding_similarity.py`
  - Contains full embedding similarity analysis for the corpus.

- `Week21_Engineering/Implementation4/Vector_Search/vector_search.py`
  - Computes Cosine Top-5 and Euclidean Top-5 using the same query embedding.

- `Week21_Engineering/Implementation5/Embedding_Search/embedding_search.py`
  - Executes embedding dot-product ranking for semantic retrieval.

- `Week21_Engineering/Implementation6/Gradient_Descent/gradient_descent_demo.py`
  - Provides a gradient descent demonstration used in the UI.

- `Week21_Engineering/Implementation7/Embedding_Failure_Analysis/embedding_failure_analysis.py`
  - Compares retrieval outputs across embeddings, cosine, euclidean, and TF-IDF to identify failure cases.

## Data flow

1. User submits a query to `/`.
2. `prompt_filter.filter_prompt()` validates the query.
3. If valid, `app.py` calls:
   - `tfidf_search.search(query)`
   - `vector_search.top_k(query)`
   - `vector_search.euclidean_search(query)`
   - `embedding_search.search2(query)`
4. Results are rendered in the web UI.
5. `record.add_record()` logs the query and results status.

## Diagram

- User → Flask `/` route → `prompt_filter`
- If OK → search modules:
  - TF-IDF
  - Cosine
  - Euclidean
  - Embedding
- Results → UI
- Errors → UI error message
