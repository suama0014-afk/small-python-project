# To-Do List (Task Tracker)

A simple command-line task manager written in Python. Add tasks, view them, update their status, and delete them from an interactive menu.

## Features

- Add a new task (new tasks start with the status `pending`)
- Display all tasks with their ID, title, and status
- Update the status of a task (for example `pending`, `in progress`, `done`)
- Delete a task by its ID
- Basic input handling: task IDs must be whole numbers, and a clear message is shown when an ID does not exist

## Tech Stack

- Python 3 (standard library only, no external dependencies)

## Getting Started

**Requirements:** Python 3.9 or newer (tested with Python 3.12)

```bash
git clone https://github.com/suama0014-afk/small-python-project.git
cd small-python-project/To_do_list
python To_do_list.py
```

> On some systems the command is `python3` instead of `python`.

## Usage

When the program starts, it shows a menu:

```
--- Task Tracker ---
1. Add task
2. display tasks
3. update task
4. delete task
5. Exit
```

Example session:

```
Enter your choice (1-5): 1
Enter task name: Buy groceries
Enter your choice (1-5): 1
Enter task name: Study Python
Enter your choice (1-5): 3
Enter task id: 1
Enter the new status: done
Enter your choice (1-5): 2
ID:1 title:Buy groceries status:done
ID:2 title:Study Python status:pending
```

## How It Works

Tasks are stored in a dictionary where each key is the task ID and each value holds the title and status:

```python
{1: {"title": "Buy groceries", "status": "done"},
 2: {"title": "Study Python", "status": "pending"}}
```

A new task gets the ID `highest existing ID + 1` (or `1` when the list is empty). The logic is split into small, documented functions with type hints:

| Function | Purpose |
|----------|---------|
| `add_task` | Add a new task |
| `delete_task` | Remove a task by ID |
| `update_task_status` | Change a task's status |
| `display_tasks` | Print all tasks |
| `main` | Run the interactive menu |

## Limitations and Future Improvements

- Tasks are kept in memory only, so they are lost when the program exits. Saving to a JSON or CSV file would make them persistent.
- The status is free text. Restricting it to a fixed set of values would avoid typos.
- Unit tests could be added for the task functions.

## Author

Osama Mohammed Abdalazim Siyd
