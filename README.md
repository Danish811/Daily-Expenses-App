# Daily Expenses Sharing Application

## Overview
The Daily Expenses Sharing Application is a backend service designed to help users manage and split expenses among groups. It allows for creating users, adding expenses with different splitting methods, and generating balance sheets.

## Features
- User Management: Create and retrieve user details
- Expense Management: Add expenses with three splitting methods:
  - Equal Split
  - Exact Amount Split
  - Percentage Split
- Expense Retrieval: Get individual user expenses and overall expenses
- Balance Sheet: Generate a downloadable balance sheet

## Technologies Used
- Python 3.7+
- Flask
- SQLAlchemy
- SQLite (default database, configurable)

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/Danish811/Daily-Expenses-App
   cd Daily-Expenses-App
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   - The application uses SQLite by default. 
   - To use a different database, set the `DATABASE_URL` environment variable.

5. Initialize the database:
   ```
   flask db upgrade
   ```

## Running the Application

1. Start the application:
   ```
   python run.py
   ```

2. The application will run on `http://127.0.0.1:5000/` by default.

## API Endpoints

### User Endpoints
- Create User: `POST /api/users`
- Get User: `GET /api/users/<user_id>`

### Expense Endpoints
- Add Expense: `POST /api/expenses`
- Get User Expenses: `GET /api/expenses/user/<user_id>`
- Get All Expenses: `GET /api/expenses`
- Get Balance Sheet: `GET /api/expenses/balance-sheet`

## Usage

To interact with the API, you can use tools like Postman or write a simple Python script using the `requests` library. Here's a basic example of how to create a user:

```python
import requests

BASE_URL = "http://127.0.0.1:5000/api"

user_data = {
    "email": "john@example.com",
    "name": "John Doe",
    "mobile": "1234567890"
}

response = requests.post(f"{BASE_URL}/users", json=user_data)
print(response.json())
```

## Error Handling

The API returns appropriate HTTP status codes along with error messages in case of failures. Common status codes:

- 200: Successful operation
- 400: Bad request (e.g., invalid input)
- 404: Resource not found
- 500: Internal server error

## Contributing

Project Link: [https://github.com/Danish811/Daily-Expenses-App](https://github.com/Danish811/Daily-Expenses-App)

Contributions to the Daily Expenses Sharing Application are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Python](https://www.python.org/)