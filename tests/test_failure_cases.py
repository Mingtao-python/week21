import unittest

from Week21_Engineering.Implementation7.Embedding_Failure_Analysis.embedding_failure_analysis import find_failure_cases


class FailureCasesTests(unittest.TestCase):
    def test_find_failure_cases_returns_structured_list(self):
        cases = find_failure_cases("bank", expected_ids=["doc_007", "doc_010"])
        self.assertIsInstance(cases, list)
        for case in cases:
            self.assertIn("summary", case)
            self.assertIn("query", case)
            self.assertIn("analysis", case)
            self.assertIn("likely_reason", case)
            self.assertIn("recommendation", case)

    def test_find_failure_cases_checks_expected_ids(self):
        cases = find_failure_cases("machine learning", expected_ids=["doc_002"])
        self.assertTrue(any(case["expected_document"] == "doc_002" for case in cases))


if __name__ == "__main__":
    unittest.main()
