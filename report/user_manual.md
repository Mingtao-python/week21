# User Manual

## Getting started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Flask app:
   ```bash
   python app.py
   ```
3. Open the browser at `http://127.0.0.1:5000`.

## How to use the application

- Enter a natural language query in the search box.
- The app returns four Top-5 ranked result lists:
  - TF-IDF
  - Cosine similarity
  - Euclidean distance
  - Embedding search
- Use the side-by-side comparison to inspect ranking differences.
- The UI is designed to surface algorithmic differences rather than provide a single consolidated score.

## Supported query types

- English queries
- Chinese queries
- Spanish queries
- French queries
- Mixed Unicode queries

## Prompt filter behavior

- The prompt filter allows normal Unicode text.
- It blocks control characters and zero-width characters.
- It also blocks explicit bypass phrases such as `ignore previous instructions`.

## Notes

- If a query is rejected, the page shows an error message explaining the block reason.
- The app is built for demonstration and algorithm comparison, not as a production LLM system.
