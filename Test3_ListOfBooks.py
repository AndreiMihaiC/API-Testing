import unittest
from Simple_Books_Request import SimpleBooksRequest


class GetAllBooks(unittest.TestCase):
    def setUp(self):
        self.books_api = SimpleBooksRequest()

    def test_get_All_books(self):
        response = self.books_api.get_all_books()
        actual_code_response = response.status_code
        expected_code_response = 200
        assert actual_code_response is expected_code_response, f"Expected code is {expected_code_response}, actual code is {actual_code_response}"

    def test_total_books(self):
        response = self.books_api.get_all_books()
        actual_number_result = len(response.json())
        expected_numerb_result = 6
        assert actual_number_result is expected_numerb_result, f"Expected number of books {expected_numerb_result}, actual number of books: {actual_number_result}"

    def test_get_all_books_filtered_by_limit(self):
        response = self.books_api.get_all_books(limit=4)
        actual_books_returned = len(response.json())
        expected_books_returned = 4
        assert actual_books_returned is expected_books_returned, f"Expected returned books: {expected_books_returned}, actual books returned: {actual_books_returned}"

    def test_get_all_books_filtered_by_type(self):
        response = self.books_api.get_all_books(book_type="fiction")
        actual_books_returned = len(response.json())
        expected_books_returned = 4
        assert actual_books_returned is expected_books_returned, f"Expected returned books: {expected_books_returned}, actual books returned: {actual_books_returned}"
        expected_type = "fiction"
        for i in range(len(response.json())):
            current_book = response.json()[i]
            actual_type = current_book["type"]
            assert actual_type == expected_type, f"Expected type for book {current_book['name']}"
            # self.assertEqual(expected_type, actual_type, f"Expected type for book {current_book['name']}")

    def test_get_all_books_filtered_by_another_type(self):
        response = self.books_api.get_all_books(book_type="non-fiction")
        actual_books_returned = len(response.json())
        expected_books_returned = 2
        assert actual_books_returned is expected_books_returned, f"Expected returned books: {expected_books_returned}, actual books returned: {actual_books_returned}"
        expected_type = "non-fiction"
        for i in range(len(response.json())):
            current_book = response.json()[i]
            actual_type = current_book["type"]
            assert actual_type == expected_type, f"Expected type for book {current_book['name']}"

    def test_get_all_books_filtered_by_negative_limit(self):
        response = self.books_api.get_all_books(limit=-1)
        actual_books_returned = len(response.json())
        expected_books_returned = 1
        assert actual_books_returned is expected_books_returned, f"Expected returned books: {expected_books_returned}, actual books returned: {actual_books_returned}"
