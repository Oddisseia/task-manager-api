from src import database


class Task(database.Model):
    __tablename__ = "task"

    task_id = database.Column(database.Integer, primary_key=True, nullable=False, unique=True)
    description = database.Column(database.String(), nullable=False)
    start_date = database.Column(database.DateTime, nullable=False)
    end_date = database.Column(database.DateTime, nullable=False)

    def to_json(self):
        return {
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date
        }
