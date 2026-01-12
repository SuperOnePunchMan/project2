# Todo API Project

## Overview

This project is a RESTful API for managing a Todo list built with Flask and Flask-RESTful. The goal is to create a fully functional API that allows users to create, read, update, and delete (CRUD) todo items. This is a learning project with fill-in-the-gaps to test your understanding of Flask, SQLAlchemy, and RESTful APIs.

## Project Structure

```
project2/
├── api/
│   ├── __init__.py          # Flask app factory
│   ├── config/
│   │   ├── __init__.py
│   │   ├── config.py        # Configuration settings
│   │   └── db.py            # Database instance
│   ├── model/
│   │   └── todo.py          # Todo model
│   └── resources/
│       ├── __init__.py
│       └── todo.py          # API resources
├── main.py                  # Entry point
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## Setup Instructions

1. **Clone or navigate to the project directory**

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set environment variables** (optional):
   Create a `.env` file in the root directory:
   ```
   SECRET_KEY=your_secret_key_here
   DATABASE_URL=sqlite:///todos.db
   DEBUG=True
   ```

6. **Run the application**:
   ```bash
   python main.py
   ```

   The API will be available at `http://localhost:5000`

## Tasks to Complete

### 1. Complete the Todo Model (`api/model/todo.py`)

The Todo model is partially implemented. You need to:

- Ensure the model inherits from `db.Model`
- Add any missing fields if needed
- Implement a `to_dict()` method for JSON serialization

### 2. Implement API Resources (`api/resources/todo.py`)

Complete the following methods in the `TodoResource` and `TodoListResource` classes:

#### TodoListResource
- `get()`: Return all todos as a JSON list
- `post()`: Create a new todo from request data

#### TodoResource
- `get(todo_id)`: Return a specific todo by ID
- `put(todo_id)`: Update an existing todo
- `delete(todo_id)`: Delete a todo by ID

### 3. Handle Errors and Validation

- Add proper error handling for invalid requests
- Validate input data
- Return appropriate HTTP status codes

## API Endpoints

Once completed, your API should support these endpoints:

- `GET /todos` - Get all todos
- `POST /todos` - Create a new todo
- `GET /todos/<id>` - Get a specific todo
- `PUT /todos/<id>` - Update a todo
- `DELETE /todos/<id>` - Delete a todo

### Request/Response Examples

#### Create Todo
```bash
POST /todos
Content-Type: application/json

{
  "title": "Learn Flask",
  "description": "Study Flask framework",
  "completed": false
}
```

#### Response
```json
{
  "id": 1,
  "title": "Learn Flask",
  "description": "Study Flask framework",
  "completed": false,
  "created_at": "2023-01-12T10:00:00Z"
}
```

## Learning Objectives

By completing this project, you will learn:

- Flask application structure and factory pattern
- SQLAlchemy ORM for database operations
- Flask-RESTful for building REST APIs
- Request parsing and validation
- JSON serialization
- HTTP methods and status codes

## Hints

- Use `db.session.add()` and `db.session.commit()` for database operations
- Use `todo_parser.parse_args()` to get request data
- Return dictionaries from resource methods (Flask-RESTful handles JSON conversion)
- Use `abort(404)` for not found errors
- Test your API with tools like Postman 

## Next Steps

After completing the basic CRUD operations:

- Add user authentication
- Implement pagination for the todo list
- Add filtering and sorting
- Create a frontend interface
- Deploy to a cloud platform

Good luck! If you get stuck, refer to the Flask and SQLAlchemy documentation.