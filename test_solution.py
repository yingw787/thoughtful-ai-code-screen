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

    def test_special_if_heavy(self):
        self.assertEqual(sort(1, 1, 1, 30), "SPECIAL")

    def test_special_if_bulky(self):
        self.assertEqual(sort(160, 1, 1, 1), "SPECIAL")
        self.assertEqual(sort(1, 160, 1, 1), "SPECIAL")
        self.assertEqual(sort(1, 1, 160, 1), "SPECIAL")
        self.assertEqual(sort(100, 100, 100, 1), "SPECIAL")

    def test_rejected(self):
        self.assertEqual(sort(160, 1, 1, 30), "REJECTED")
        self.assertEqual(sort(100, 100, 100, 30), "REJECTED")
