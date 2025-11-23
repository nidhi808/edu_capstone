# src/task_tool.py - simple task creation stub (writes tasks.json)
import json
import os

# tasks.json will live in repo root
TASKS_FILE = os.path.join(os.path.dirname(__file__), "..", "tasks.json")

def create_task(title: str, assignee: str = "unknown", due_date: str = None, meta: dict = None):
    """
    Append a task to tasks.json and return the created task entry.
    This is a stub for demo; replace with real API calls for production.
    """
    try:
        # Read existing tasks if any
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            tasks = json.load(f)
    except Exception:
        tasks = []

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "assignee": assignee,
        "due_date": due_date,
        "meta": meta or {}
    }
    tasks.append(task)

    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

    return task
