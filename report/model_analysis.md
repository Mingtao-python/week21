# Model Analysis Report

## Models used

- Embedding model: `sentence-transformers/all-MiniLM-L6-v2`
- TF-IDF model: `sklearn.feature_extraction.text.TfidfVectorizer`
- Vector similarity helpers: Cosine and Euclidean from `Week21_Engineering/Implementation1/Similarity_Engine/similarity.py`

## Algorithm comparisons

- TF-IDF is keyword-based and ranks by term relevance.
- Cosine similarity ranks normalized vector similarity higher for closer semantic vectors.
- Euclidean distance ranks lower distance values for closer semantic vectors.
- Embedding dot-product ranks documents by semantic similarity of sentence vectors.

## What the results show

- Cosine and embedding rankings are often similar because both use vector angles and dot-product semantics.
- Euclidean ranking can differ because it preserves absolute vector distance; this matters when embedding magnitude varies.
- TF-IDF differs substantially for queries with strong lexical overlap.

## Practical guidance

- Use Cosine Top-5 to understand similarity under normalized vector space.
- Use Euclidean Top-5 to compare raw distance-based ranking.
- Use TF-IDF Top-5 for exact keyword matches.
- Use Embedding Top-5 for semantic generalization.

## Limitations

- The dataset is small, so ranking behavior is illustrative rather than production-grade.
- A limited embedding model and corpus size may produce noisy rankings on ambiguous queries.
- Euclidean and Cosine differences are more visible on longer, semantically rich queries.
