# Testing Results

## Machine-readable verification

- `tests/results_20_queries.json` contains 20 queries with expected output IDs and Top-5 results for all four algorithms.
- Each query includes:
  - `query`
  - `expected_ids`
  - `tfidf_top5`
  - `cosine_top5`
  - `euclidean_top5`
  - `embedding_top5`
  - `pass`
  - `notes`

## Test coverage added

- `tests/test_prompt_filter.py` for prompt filter acceptance and rejection behavior.
- `tests/test_multilingual_input.py` for Chinese, Spanish, and French query validation.
- `tests/test_dataset_validation.py` for dataset integrity.
- `tests/test_20_queries.py` for validating 20 query outputs against saved results.
- `tests/test_failure_cases.py` for retrieval failure and ranking comparison cases.
- `tests/test_euclidean_vs_cosine.py` for Cosine and Euclidean ranking differences.

## CI execution

- GitHub Actions runs on `ubuntu-latest` with Python 3.12.
- Dependencies are installed from `requirements.txt`.
- All tests in `tests/` are executed with `python -m pytest tests -q`.

## Current reliability statement

- The current security and retrieval claims are based on the available test suite and sample dataset.
- The product does not claim `100% security`; it reports results on the current test set only.
