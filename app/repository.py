"""
Data access layer for TaskFlow.

Per ADR-001 (docs/adr/001-repository-pattern.md), ALL database access must
go through this module. No other file should import sqlite3 directly.
"""

import sqlite3
from contextlib import contextmanager

DB_PATH = "taskflow.db"


@contextmanager
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                done INTEGER NOT NULL DEFAULT 0,
                priority TEXT NOT NULL DEFAULT 'normal'
            )
            """
        )


class TaskRepository:
    """All task persistence goes through this class."""

    def list_tasks(self):
        with get_connection() as conn:
            rows = conn.execute("SELECT * FROM tasks ORDER BY id").fetchall()
            return [dict(row) for row in rows]

    def get_task(self, task_id):
        with get_connection() as conn:
            row = conn.execute(
                "SELECT * FROM tasks WHERE id = ?", (task_id,)
            ).fetchone()
            return dict(row) if row else None

    def create_task(self, title, priority="normal"):
        with get_connection() as conn:
            cursor = conn.execute(
                "INSERT INTO tasks (title, done, priority) VALUES (?, 0, ?)",
                (title, priority),
            )
            row = conn.execute(
                "SELECT * FROM tasks WHERE id = ?", (cursor.lastrowid,)
            ).fetchone()
            return dict(row) if row else None

    def update_task(self, task_id, **fields):
        if not fields:
            return self.get_task(task_id)
        columns = ", ".join(f"{key} = ?" for key in fields)
        values = list(fields.values()) + [task_id]
        with get_connection() as conn:
            conn.execute(f"UPDATE tasks SET {columns} WHERE id = ?", values)
            row = conn.execute(
                "SELECT * FROM tasks WHERE id = ?", (task_id,)
            ).fetchone()
            return dict(row) if row else None

    def delete_task(self, task_id):
        with get_connection() as conn:
            conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
