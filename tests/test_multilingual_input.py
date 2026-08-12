import unittest

from Week21_Engineering.Implementation4.Vector_Search.vector_search import top_k, euclidean_search
from Week21_Engineering.Implementation5.Embedding_Search.embedding_search import search2
from Week21_Engineering.Implementation2.TFIDF_Retrieval.tfidf_search import search as tfidf_search


class MultilingualInputTests(unittest.TestCase):
    def test_chinese_query_returns_results(self):
        query = "机器学习"
        self.assertGreaterEqual(len(tfidf_search(query, k=5)), 1)
        self.assertGreaterEqual(len(top_k(query, k=5)), 1)
        self.assertGreaterEqual(len(euclidean_search(query, k=5)), 1)
        self.assertGreaterEqual(len(search2(query, k=5)), 1)

    def test_spanish_query_returns_results(self):
        query = "aprendizaje automático"
        self.assertGreaterEqual(len(tfidf_search(query, k=5)), 1)
        self.assertGreaterEqual(len(top_k(query, k=5)), 1)
        self.assertGreaterEqual(len(euclidean_search(query, k=5)), 1)
        self.assertGreaterEqual(len(search2(query, k=5)), 1)

    def test_french_query_returns_results(self):
        query = "recherche sémantique"
        self.assertGreaterEqual(len(tfidf_search(query, k=5)), 1)
        self.assertGreaterEqual(len(top_k(query, k=5)), 1)
        self.assertGreaterEqual(len(euclidean_search(query, k=5)), 1)
        self.assertGreaterEqual(len(search2(query, k=5)), 1)


if __name__ == "__main__":
    unittest.main()
