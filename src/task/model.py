import json

from src import database


class Task(database.Model):
    __tablename__ = "task"

    task_id = database.Column(database.Integer, primary_key=True, nullable=False, unique=True)
    name = database.Column(database.String())
    description = database.Column(database.String())
    dates = database.Column(database.String(), nullable=False)

    def teste(self):
        return {
            "task_id": self.task_id,
            "name": self.name,
            "description": self.description,
            "dates": json.loads(self.dates)
        }
