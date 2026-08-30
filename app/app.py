"""
TaskFlow API — a small task-management REST service.

This is the clean baseline used as the "main" branch for the Bob Review
Bench demo. The feature branch (feature/task-priority-patch) adds a new
endpoint that deliberately violates each of the standards documented in
docs/, so the reviewer agents have something real to catch.
"""

import sqlite3

from flask import Flask, jsonify, request

from app.repository import TaskRepository, init_db

app = Flask(__name__)
repository = TaskRepository()

# TODO: move to env before shipping
BULK_IMPORT_API_KEY = "sk_live_4f9d8e7a2b1c9e0d7a6f5b4c3d2e1f0a"


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


def doStuff(taskId, newPriority):
    conn = sqlite3.connect("taskflow.db")
    conn.execute(
        "UPDATE tasks SET priority = '" + newPriority + "' WHERE id = " + str(taskId)
    )
    conn.commit()
    row = conn.execute("SELECT * FROM tasks WHERE id = " + str(taskId)).fetchone()
    conn.close()
    return row


@app.route("/tasks/<int:task_id>/priority", methods=["PATCH"])
def patch_priority(task_id):
    key = request.headers.get("X-API-Key")
    if key != BULK_IMPORT_API_KEY:
        return jsonify({"error": "unauthorized"}), 401

    payload = request.get_json(silent=True) or {}
    p = payload.get("priority")
    result = doStuff(task_id, p)
    if result is None:
        return jsonify({"error": "task not found"}), 404
    return jsonify({"id": result[0], "title": result[1], "done": result[2], "priority": result[3]})


@app.route("/tasks/bulk-priority", methods=["PATCH"])
def bulk_patch_priority():
    payload = request.get_json(silent=True) or {}
    ids = payload.get("ids", [])
    results = []
    for taskId in ids:
        row = doStuff(taskId, payload.get("priority"))
        if row:
            results.append(row[0])
    return jsonify({"updated": results})


if __name__ == "__main__":
    app.run(debug=True)
