import unittest

from solution import sort


class TestCheckSortingCriteria(unittest.TestCase):
    def test_valid_inputs(self):
        with self.assertRaises(ValueError):
            sort("str", 1, 1, 1)
        with self.assertRaises(ValueError):
            sort(1, "str", 1, 1)
        with self.assertRaises(ValueError):
            sort(1, 1, "str", 1)
        with self.assertRaises(ValueError):
            sort(1, 1, 1, "str")

        with self.assertRaises(ValueError):
            sort(-1, 1, 1, 1)
        with self.assertRaises(ValueError):
            sort(1, -1, 1, 1)
        with self.assertRaises(ValueError):
            sort(1, 1, -1, 1)
        with self.assertRaises(ValueError):
            sort(1, 1, 1, -1)

    def test_standard(self):
        self.assertEqual(sort(1, 1, 1, 1), "STANDARD")

    def test_special(self):
        self.assertEqual(sort(1, 1, 1, 30), "SPECIAL")

    def test_rejected(self):
        self.assertEqual(sort(160, 1, 1, 30), "REJECTED")
