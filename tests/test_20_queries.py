import json
import os
import unittest

from Week21_Engineering.Implementation2.TFIDF_Retrieval.tfidf_search import search as tfidf_search
from Week21_Engineering.Implementation4.Vector_Search.vector_search import top_k, euclidean_search
from Week21_Engineering.Implementation5.Embedding_Search.embedding_search import search2


class QueryResultConsistencyTests(unittest.TestCase):
    def setUp(self):
        fixture_path = os.path.join(os.path.dirname(__file__), "results_20_queries.json")
        with open(fixture_path, encoding="utf-8") as handle:
            self.results = json.load(handle)

    def test_saved_results_match_current_outputs(self):
        for item in self.results:
            query = item["query"]
            tfidf_top5 = [text for text in item["tfidf_top5"]]
            cosine_top5 = [text for text in item["cosine_top5"]]
            euclidean_top5 = [text for text in item["euclidean_top5"]]
            embedding_top5 = [text for text in item["embedding_top5"]]

            self.assertEqual(
                [text for text, _ in tfidf_search(query, k=5)],
                tfidf_top5
            )
            self.assertEqual(
                [text for text, _ in top_k(query, k=5)],
                cosine_top5
            )
            self.assertEqual(
                [text for text, _ in euclidean_search(query, k=5)],
                euclidean_top5
            )
            self.assertEqual(
                [text for text, _ in search2(query, k=5)],
                embedding_top5
            )


if __name__ == "__main__":
    unittest.main()
