import requests


class SimpleBooksRequest:
    BASE_URL = "https://simple-books-api.glitch.me"
    API_STATUS_ENDPOINT = "/status"
    GET_SINGLE_BOOKS_ENDPOINT = "/books/"
    ID_SINGLE_BOOK = 2
    GET_ALL_BOOKS_ENDPOINT = "/books"
    ORDER_BOOK = "/orders"


    def get_api_status(self):
        api_status_url = self.BASE_URL + self.API_STATUS_ENDPOINT
        response = requests.get(api_status_url)
        return response

    def get_single_book(self):
        get_single_book = f"{self.BASE_URL}{self.GET_SINGLE_BOOKS_ENDPOINT}{self.ID_SINGLE_BOOK}"
        response = requests.get(get_single_book)
        return response

    def get_all_books(self, limit="", book_type=""):
        get_all_books_url = self.BASE_URL + self.GET_ALL_BOOKS_ENDPOINT
        if limit != "" and book_type == "":
            get_all_books_url += f"?limit={limit}"
        if book_type != "" and limit == "":
            get_all_books_url += f"?type={book_type}"
        if limit != "" and book_type != "":
            get_all_books_url += f"?limit={limit}&type{book_type}"
        response = requests.get(get_all_books_url)
        return response

    def post_order_book(self):
        post_order_book = self.BASE_URL + self.ORDER_BOOK
        data = {
            "bookId": 5,
            "customerName": "Paul Olteanu"
        }
        response = requests.get(post_order_book)
        return response

    def get_all_book_orders(self):
        get_all_book_orders = self.BASE_URL + self.API_STATUS_ENDPOINT
        response = requests.get(get_all_book_orders)
        if response.status_code == 200:
            ordered_books = response.json()
            return ordered_books
        else:
            print(f"Error fetching ordered books. Status code: {response.status_code}")
            return None


