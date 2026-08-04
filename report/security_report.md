# Project Report
## Model Analysis Report

1. Sucessful querys
- The project sucessfully handles queries such as "machine learning", "deap neural networks", "semantic search", "bank", and many more.
- Tests in `tests/test_search.py` and `tests/test_product_flow.py` verify that all retrieval modules return at least 3 results for these queries.
- The app is designed to compar TF-IDF, cosine similarity, and embedding-style search side by side.

2. Query failures
- Failures are mainly caused by ambiguous queries and limited dataset coverage.
- Example: the query "bank" can mean financial institution or river bank, so the result set may be inconsistent across TF-IDF and embedding search.
- Another failure factor is sparse data in `dataset.json`, which makes top-K results unstable for some domain-specific queries.

3. Model names
- Embedding model: `sentence-transformers/all-MiniLM-L6-v2`.
- TF-IDF model: `sklearn.feature_extraction.text.TfidfVectorizer`.
- The project also includes a deterministic fallback embedding strategy when the pretrained model is unavailable.

4. Real scores
- Embedding search score is computed by dot product between `document_vectors` and the query embedding `qv`.
- TF-IDF score is computed as `(X * q.T).toarray().flatten()`.
- Tests verify that search results return float scores and at least 3 ranked documents for each query.
- This project currently reports retrieval availability rather than precise accuracy or recall metrics.

5. Polysemy errors
- Polysemy is a key error mode: words like "bank" have multiple meanings.
- Embedding search tends to return semantically related documents, while TF-IDF returns keyword-matching documents.
- When queries are ambiguous and lack context, both search methods can return noisy or mismatched results.

6. TF-IDF vs Embedding comparison
- Core concept
  - TF-IDF: word frequency with inverse document frequency, based on surface matching.
  - Embedding: vector representation of semantics, based on meaning and context.

- Dependence on exact terms
  - TF-IDF: strong dependence on exact words appearing in the text.
  - Embedding: less dependence on exact wording, better at synonyms.

- Semantic understanding
  - TF-IDF: cannot understand synonyms or context.
  - Embedding: can capture similar meaning and semantic relationships.

- Multilanguage and morphology
  - TF-IDF: weaker for other languages and word forms.
  - Embedding: stronger on multilingual and inflected forms.

- Context awareness
  - TF-IDF: no real context understanding.
  - Embedding: can reflect sentence-level or paragraph-level semantics.

- Project conclusion
  - Embedding is stronger for semantic search and fuzzy queries.
  - TF-IDF is still useful for exact keyword matching and low-data scenarios.

7. How to improve search quality
- Use a larger or stronger embedding model.
- Add a reranker to combine TF-IDF and embedding scores.
- Improve query text preprocessing and separators.
- Add more professional or domain-specific documents to `dataset.json`.
- Use RAG for better retrieval augmentation.
- Use FAISS or Milvus for scalable vector search.

## Security Analysis Report

1. Source of prompt injection risk
- User input.
- External context or metadata.
- RAG content returned from retrieval.

2. Prompt injection attack path
- User → Input → Embedding → Retrieval → LLM → Output.
- The main attack surfaces are user input and the LLM prompt itself.
- Embedding does not enforce rules; it only converts text into vectors and can still influence retrieval.

3. Why attacks can succeed
- LLMs often follow prompt instructions.
- They cannot reliably distinguish between good and malicious text.
- They cannot consistently separate system prompt from user prompt.
- They may not know when to trust or ignore injected content.

4. How prompt filtering reduces risk
- Prompt filtering can limit input length.
- It can detect and reject obvious malicious or injection-like strings.
- It can clean input text before retrieval.
- It can help protect the system prompt and retrieval pipeline.

5. Remaining system risk
- Filters can only block basic attacks.
- They may fail against complex or subtle prompt injection.
- They cannot fully prevent attacks that combine multiple vectors.
- They cannot fully block RAG poisoning or Unicode/encoding tricks.

6. How to improve security
- Use safer or more robust models.
- Add more layers of filtering.
- Limit model authority and the scope of generated responses.
- Use a better RAG pipeline with source validation.
- Monitor and defend against structured injection like JSON or special tokens.  
