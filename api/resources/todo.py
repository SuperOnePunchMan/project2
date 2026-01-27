from flask_restful import Resource, reqparse
from ..model.todo import Todo
from ..config.db import db
import sqlite3
from flask import request
# Parser for Todo input
todo_parser = reqparse.RequestParser()
todo_update= reqparse.RequestParser()
todo_update.add_argument('completed',type=bool, required=True)
todo_parser.add_argument('title', type=str, required=True, help='Title is required')
todo_parser.add_argument('description', type=str)
todo_parser.add_argument('completed', type=bool, default=False)

class TodoListResource(Resource):
    def get(self):
        try:
            todo= Todo.query.all()
            return({
                "status":"success",
                "data":[Todo.to_dict()],
                "status_code":200
            })
        except Exception as e:
            return{
                "status":"failed",
                "message": str(e)
            }
        

        # TODO: Retrieve all todos from the database
        # Return a list of todos in JSON format

    def post(self):
        try:
            data= todo_parser.parse_args()
            description= data["description"]
            completed= data["completed"]
            title=data["title"]
            
            new_todo= Todo(
                title=title,
                description=description,
                completed=completed
            ) 

            db.session.add(new_todo)
            db.session.commit()
            return({
                "status":"success",
                "data":new_todo.to_dict(),
                "Status_code":201
            }),
        except Exception as e:
            print(e)
            return{
                "status":"failed",
                "message": str(e)
            }
        # TODO: Parse the request arguments
        # Create a new Todo instance
        # Save it to the database
        # Return the created todo with status 201


class TodoResource(Resource):
    def get(self, todo_id):
        try:
            todo=Todo.query.filter_by(id=todo_id).first()
            if not todo:
                return{"message": "todo not found"},404
            return{
                "status":"success",
                "data": todo.to_dict(),
            },200
        except Exception as e:
            return{
                "status":"failed",
                "message": str(e)
            }


        
        # TODO: Retrieve a specific todo by id
        # If not found, return 404
        # Return the todo in JSON format
        

    def put(self, todo_id):
        try:
            fix=Todo.query.filter_by(id=todo_id).first()
            if not fix:
                return{"message": "Fix not found"},404
            data=todo_update.parse_args()
            status=data["completed"]
            fix.completed= data.completed
            db.session.commit()
            db.session.refresh
            return{
                "status":"failed",
                "message":fix.to_dict()
            }
        except Exception as e:
            return{
                "status":"failed",
            "message": str(e)
            }
        

        
        # TODO: Retrieve the todo by id
        # Parse the update arguments
        # Update the todo fields
        # Save to database
        # Return the updated todo
        

    def delete(self, todo_id):
        try:
            todo_to_delete= Todo.query.filter_by(id=todo_id).first()
            if not todo_to_delete:
                return{
                    "status":"failed",
                    "message":"Todo not found"
                },404
            db.session.delete(todo_to_delete)
            db.session.commit()
            return{
                "status":"success",
                "message":"Todo deleted succesfully"
            },200
        except Exception as e:
            return{
                "status":"failed",
                "message":str(e)
            }

        # TODO: Retrieve the todo by id
        # Delete it from the database
        # Return success message