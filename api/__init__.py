from flask import Flask
from flask_restful import Api
from .config.config import config_dict
from .config.db import db

def create_app(config= config_dict['development']):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    api = Api(app)

    # TODO: Import and add your resources here
    from .resources.todo import TodoResource, TodoListResource
    api.add_resource(TodoListResource, '/todos')
    api.add_resource(TodoResource, '/todos/<int:todo_id>')

    # TODO: Create all tables within the app context
    with app.app_context():
        db.create_all()

    return app