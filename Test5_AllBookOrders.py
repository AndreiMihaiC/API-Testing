import unittest
from Simple_Books_Request import SimpleBooksRequest


class AllBookOrders(unittest.TestCase):
    def setUp(self):
        self.books_api = SimpleBooksRequest()

    def test_get_all_number_books_orders(self):
        ordered_books = self.books_api.get_all_book_orders()
        if ordered_books:
            print(f"Numărul de cărți comandate: {len(ordered_books)}")
        else:
            print("Nu s-au putut obține datele despre cărți comandate.")




