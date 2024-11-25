import unittest

from src.validators import validate_year, validate_book_id


class TestValidators(unittest.TestCase):

    def test_validate_year(self):
        self.assertTrue(validate_year("1990"))
        self.assertFalse(validate_year("199f"))
        self.assertFalse(validate_year("2500"))

    def test_validate_book_id(self):
        self.assertTrue(validate_book_id("10"))
        self.assertFalse(validate_book_id("one"))

