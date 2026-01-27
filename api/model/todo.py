from ..config.db import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Todo {self.title}>'

    # TODO: Implement to_dict() method for JSON serialization
    def to_dict(self):
        return{
            "title": self.title,
            "description":self.description,
            "completed":self.completed,
            "created_at":self.created_at.isoformat()
        }