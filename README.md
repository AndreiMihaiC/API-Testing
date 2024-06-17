# Simple Books API #

The API is available at `https://simple-books-api.glitch.me`

## Endpoints ##

GET `/status`

Returns the status of the API.

![API Status](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/d465dd6d-d92e-45c9-90a8-8a683c5f1d6b)

### List of books ###

GET `/books`

Returns a list of books.

Optional query parameters:

- type: fiction or non-fiction
- limit: a number between 1 and 20.

![List of books](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/ab6cabd0-d3db-44ad-8ba9-0e85df9be1c9)

Error: "Invalid value for query parameter 'type'".

![List of books - error](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/0760c231-c11a-4d52-b459-ff2e446740a3)


### Get a single book ###

GET `/books/:bookId`

Retrieve detailed information about a book.

![Get a single book](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/cedd0975-837c-404c-8b75-f689c07f5c13)

Error "No book with id 10":

![Get a single book - error](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/60917d6a-2b9c-4f2f-bfb6-a461766e6148)

### Submit an order ###

POST `/orders`

Allows you to submit a new order. Requires authentication.

The request body needs to be in JSON format and include the following properties:

 - `bookId` - Integer - Required
 - `customerName` - String - Required

The response body will contain the order Id.

![Order book](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/ca4d9b2e-0b30-4a5e-b7ff-05676c6f2c64)

Random Fullname: 

![Order book- random fullname](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/2f852e7c-9467-4a48-911f-43fe3707d46d)

Error: "book is not in stock"

![Order book- book is not in stock](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/a7562ff1-d5b9-4cf9-974d-7a7faedf3de6)

### Get all orders ###

GET `/orders`

Allows you to view all orders. Requires authentication.


![Get all book order](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/4d487450-936d-4506-9917-c16fcc9d56cc)

### Get an order ###

GET `/orders/:orderId`

Allows you to view an existing order. Requires authentication.


![Get an order](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/a9d1e315-db41-45e3-89d5-044bb1bd78c6)

### Update an order ###

PATCH `/orders/:orderId`

Update an existing order. Requires authentication.

The request body needs to be in JSON format and allows you to update the following properties:

 - `customerName` - String

![Update an order](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/54e38cc5-7e23-4b48-ade0-e6d9aba6c54d)

### Delete an order ###

DELETE `/orders/:orderId`

Delete an existing order. Requires authentication.

The request body needs to be empty.

![Delete order](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/291a1a37-ef74-4a22-b163-a07a823752b4)

## API Authentication ##

To submit or view an order, you need to register your API client.

POST `/api-clients/`

Example

 ```
 {
    "clientName": "Postman",
    "clientEmail": "valentin@example.com"
}
```

![Register_API_Client - generated token](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/55a8b6d0-855a-4887-8069-04b55f56dea9)

AccesToken:

![Register_API_Client - succes token](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/67f19e57-acae-4432-8add-c8be970836cf)








