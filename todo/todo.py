import click  # To create a Command Line Interface (CLI)
import json  # To save and load tasks from a JSON file
import os  # To check if the file exists or not

# Define the file where tasks will be stored
TODO_FILE = "todo.json"

def load_task():
    """
    Load tasks from the JSON file.
    If the file doesn't exist, return an empty list.
    """
    if not os.path.exists(TODO_FILE):  # Check if the file exists
        return []  # Return an empty list if the file is not found
    with open(TODO_FILE, "r") as file:
        try:
            return json.load(file)  # Load and return tasks from the file
        except json.JSONDecodeError:
            return []  # Return an empty list if the file is corrupt

def save_tasks(tasks):
    """
    Save tasks to the JSON file.
    """
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)  # Write tasks to the file with indentation

@click.group()
def cli():
    """
    Simple Todo List Manager.
    """
    pass  # This is required for Click to function properly as a command group

@click.command()
@click.argument("task")
def add(task):
    """
    Add a new task to the list.
    """
    tasks = load_task()  # Load existing tasks
    tasks.append({"task": task, "done": False})  # Add a new task with 'done' set to False
    save_tasks(tasks)  # Save the updated list of tasks
    click.echo(f"Task added successfully: {task}")

@click.command()
def lists():
    """
    List all the tasks.
    """
    tasks = load_task()  # Load existing tasks
    if not tasks:
        click.echo("No tasks found!")  # Display a message if there are no tasks
        return
    for index, task in enumerate(tasks, 1):  # Iterate through the tasks with an index
        status = "✅" if task['done'] else "❌"  # Mark completed tasks with a checkmark
        click.echo(f"{index}: {task['task']} [{status}]")  # Display tasks with status

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """
    Mark a task as completed.
    """
    tasks = load_task()  # Load existing tasks
    if 0 < task_number <= len(tasks):  # Ensure the task number is valid
        tasks[task_number - 1]['done'] = True  # Update the task status to completed
        save_tasks(tasks)  # Save the updated tasks list
        click.echo(f"Task {task_number} marked as completed!")
    else:
        click.echo(f"Invalid task number: {task_number}")  # Handle invalid task numbers

@click.command()
@click.argument("task_number", type=int)
def remove(task_number):
    """
    Remove a task from the list.
    """
    tasks = load_task()  # Load existing tasks
    if 0 < task_number <= len(tasks):  # Ensure the task number is valid
        removed_task = tasks.pop(task_number - 1)  # Remove the task from the list
        save_tasks(tasks)  # Save the updated tasks list
        click.echo(f"Removed task: {removed_task['task']}")
    else:
        click.echo("Invalid task number!")  # Handle invalid task numbers

# Register the commands with the CLI
cli.add_command(add)
cli.add_command(lists)
cli.add_command(complete)
cli.add_command(remove)

if __name__ == "__main__":
    cli()  # Run the CLI application
