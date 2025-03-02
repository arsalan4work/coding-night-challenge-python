# Todo List Manager

This is a simple command-line Todo List Manager built using Python and Click. The program allows users to add, list, mark as complete, and remove tasks from a todo list. The tasks are saved in a JSON file, so they persist between program runs.

## Requirements

- Python 3.6 or higher
- `click` library for creating the Command Line Interface (CLI)

You can install the required Python library using pip:

```cmd
pip install click

## To run this on cli
```cmd
uv run python todo.py add "Task Description"

## To check the list of total task
```cmd
uv run python todo.py lists

## To mark as completed task
```cmd
uv run python todo.py complete <task number>

## To remove task from file
```cmd
uv run python todo.py remove <task_number>

