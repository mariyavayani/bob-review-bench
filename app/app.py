"""
TaskFlow API — a small task-management REST service.

"""

from flask import Flask, jsonify, request

from app.repository import TaskRepository, init_db

app = Flask(__name__)
repository = TaskRepository()


@app.before_request
def ensure_db():
    init_db()


@app.route("/tasks", methods=["GET"])
def list_tasks():
    """Return all tasks."""
    return jsonify(repository.list_tasks())


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    """Return a single task by id."""
    task = repository.get_task(task_id)
    if task is None:
        return jsonify({"error": "task not found"}), 404
    return jsonify(task)


@app.route("/tasks", methods=["POST"])
def create_task():
    """Create a new task."""
    payload = request.get_json(silent=True) or {}
    title = payload.get("title")
    if not title:
        return jsonify({"error": "title is required"}), 400
    priority = payload.get("priority", "normal")
    task = repository.create_task(title, priority)
    return jsonify(task), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    """Update an existing task."""
    if repository.get_task(task_id) is None:
        return jsonify({"error": "task not found"}), 404
    payload = request.get_json(silent=True) or {}
    allowed = {"title", "done", "priority"}
    fields = {key: value for key, value in payload.items() if key in allowed}
    task = repository.update_task(task_id, **fields)
    return jsonify(task)


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """Delete a task."""
    if repository.get_task(task_id) is None:
        return jsonify({"error": "task not found"}), 404
    repository.delete_task(task_id)
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
