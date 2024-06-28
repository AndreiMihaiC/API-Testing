import unittest
from Simple_Books_Request import SimpleBooksRequest


class TestSingleBook(unittest.TestCase):
    def setUp(self):
        self.books_api = SimpleBooksRequest()

    def test_get_single_book(self):
        response = self.books_api.get_single_book()
        self.assertEqual(response.status_code, 200, "Statusul nu este 200")


