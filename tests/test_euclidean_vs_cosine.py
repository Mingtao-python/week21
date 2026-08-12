import unittest

from Week21_Engineering.Implementation4.Vector_Search.vector_search import top_k, euclidean_search


class EuclideanVsCosineTests(unittest.TestCase):
    def test_cosine_and_euclidean_rankings_differ(self):
        query = "semantic search"
        cosine_results = [text for text, _ in top_k(query, k=5)]
        euclidean_results = [text for text, _ in euclidean_search(query, k=5)]
        self.assertEqual(len(cosine_results), 5)
        self.assertEqual(len(euclidean_results), 5)
        self.assertNotEqual(cosine_results, euclidean_results)

    def test_cosine_top5_contains_relevant_documents(self):
        query = "machine learning"
        cosine_results = [text for text, _ in top_k(query, k=5)]
        self.assertIn("Machine learning is a field of artificial intelligence.", cosine_results)

    def test_euclidean_top5_contains_relevant_documents(self):
        query = "machine learning"
        euclidean_results = [text for text, _ in euclidean_search(query, k=5)]
        self.assertIn("Machine learning is a field of artificial intelligence.", euclidean_results)


if __name__ == "__main__":
    unittest.main()
