import unittest
from uv_rules import check_uv

class TestUV(unittest.TestCase):

    def test_empty_text(self):
        with self.assertRaises(ValueError):
            check_uv("")

    def test_consonants(self):
        result = check_uv("Наш клас в школі.")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["suggestion"], "у")

    def test_vowels(self):
        result = check_uv("Вона була у Одесі.")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["suggestion"], "в")

    def test_correct_text(self):
        result = check_uv("Ми були в школі.")
        self.assertEqual(len(result), 0)

if __name__ == "__main__":
    unittest.main()
