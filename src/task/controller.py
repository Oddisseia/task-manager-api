from src.task.model import Task


def list_all_tasks_controller():
    tasks = Task.query.all()
    response = []
    for task in tasks:
        response.append(task.teste())
    return response
