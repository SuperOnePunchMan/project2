from flask_restful import Resource, reqparse
from ..model.todo import Todo
from ..config.db import db

# Parser for Todo input
todo_parser = reqparse.RequestParser()
todo_parser.add_argument('title', type=str, required=True, help='Title is required')
todo_parser.add_argument('description', type=str)
todo_parser.add_argument('completed', type=bool, default=False)

class TodoListResource(Resource):
    def get(self):
        # TODO: Retrieve all todos from the database
        # Return a list of todos in JSON format
        pass

    def post(self):
        # TODO: Parse the request arguments
        # Create a new Todo instance
        # Save it to the database
        # Return the created todo with status 201
        pass

class TodoResource(Resource):
    def get(self, todo_id):
        # TODO: Retrieve a specific todo by id
        # If not found, return 404
        # Return the todo in JSON format
        pass

    def put(self, todo_id):
        # TODO: Retrieve the todo by id
        # Parse the update arguments
        # Update the todo fields
        # Save to database
        # Return the updated todo
        pass

    def delete(self, todo_id):
        # TODO: Retrieve the todo by id
        # Delete it from the database
        # Return success message
        pass