import json
import os
import unittest

from prompt_filter import filter_prompt


class DatasetValidationTests(unittest.TestCase):
    def setUp(self):
        root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        with open(os.path.join(root, "dataset.json"), encoding="utf-8") as handle:
            self.dataset = json.load(handle)

    def test_dataset_has_id_and_text_for_each_item(self):
        self.assertTrue(len(self.dataset) >= 20)
        for item in self.dataset:
            self.assertIn("id", item)
            self.assertIn("text", item)
            self.assertIsInstance(item["id"], str)
            self.assertIsInstance(item["text"], str)

    def test_dataset_text_is_not_empty(self):
        for item in self.dataset:
            self.assertGreater(len(item["text"].strip()), 0)

    def test_prompt_filter_accepts_dataset_text(self):
        for item in self.dataset[:5]:
            ok, _ = filter_prompt(item["text"])
            self.assertTrue(ok)


if __name__ == "__main__":
    unittest.main()
