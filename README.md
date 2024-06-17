# Simple Books API #

The API is available at `https://simple-books-api.glitch.me`

## Endpoints ##

GET `/status`

Returns the status of the API.

![API Status](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/c42432d6-94e7-4213-bc78-742c195a0102)

### List of books ###

GET `/books`

Returns a list of books.

Optional query parameters:

- type: fiction or non-fiction
- limit: a number between 1 and 20.

![List of books](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/e1114e8f-9278-4034-9345-7dfa484ea5cf)

Error: "Invalid value for query parameter 'type'".

![List of books - error](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/39c5c216-cb1f-45f6-adfa-fcd31bd8753c)


### Get a single book ###

GET `/books/:bookId`

Retrieve detailed information about a book.

![Get a single book](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/91573185-97b5-4072-af05-439352bdae9e)

Error "No book with id 10":

![Get a single book - error](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/f8164406-5832-4251-b906-006f2759c568)

### Submit an order ###

POST `/orders`

Allows you to submit a new order. Requires authentication.

The request body needs to be in JSON format and include the following properties:

 - `bookId` - Integer - Required
 - `customerName` - String - Required

The response body will contain the order Id.

![Order book](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/a9bf60a7-9152-47a1-912e-dc16963afdf3)

Random Fullname: 

![Order book- random fullname](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/576e7205-2a85-4625-9408-a475300afefc)

Error: "book is not in stock"

![Order book- book is not in stock](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/c699d51d-000e-44ac-a0a3-73790b62fb9c)

### Get all orders ###

GET `/orders`

Allows you to view all orders. Requires authentication.

![Get all book order](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/5acd6cef-c7ea-4a17-bd81-4cff47823269)

### Get an order ###

GET `/orders/:orderId`

Allows you to view an existing order. Requires authentication.

![Get an order](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/9b81f8ac-1284-469a-ab61-b2b1b62b7115)

### Update an order ###

PATCH `/orders/:orderId`

Update an existing order. Requires authentication.

The request body needs to be in JSON format and allows you to update the following properties:

 - `customerName` - String

![Update an order](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/e7eacbf5-2077-4a08-bdec-fdf14d172ea5)

### Delete an order ###

DELETE `/orders/:orderId`

Delete an existing order. Requires authentication.

The request body needs to be empty.

![Delete order](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/7d5551be-5c78-4a13-80a7-387a07c6d60e)

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

![Register_API_Client - generated token](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/13337460-9911-4a6b-b968-016e8c44a828)

AccesToken:

![Register_API_Client - succes token](https://github.com/AndreiMihaiC/API-Testing/assets/120325527/6216770f-66c3-49ab-a46e-40515f9547ef)








