from src.app import app
from src.task.controller import list_all_tasks_controller


@app.route("/tasks", methods=["GET"])
def list_all_tasks():
    return list_all_tasks_controller()
