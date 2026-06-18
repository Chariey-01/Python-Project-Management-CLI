# Python Project Management CLI

A small command-line project management app written in Python. It lets you create users, create projects, add tasks to projects, mark tasks as complete, and persist everything to a local JSON database.

## Features

- Add and list users
- Add and list projects
- Add tasks to a project
- Mark tasks as complete
- Validate user email addresses
- Save data in `data/database.json`
- Unit tests for the core models and project manager behavior

## Project Structure

```text
.
├── main.py                    # CLI entry point
├── data/database.json         # Local JSON data store
├── models/
│   ├── person.py              # Base person model
│   ├── user.py                # User model
│   ├── projects.py            # Project model
│   └── task.py                # Task model
├── services/project_manager.py # Main application logic
├── utils/file_handler.py      # JSON loading and saving helpers
├── tests/test_models.py       # Unit tests
└── requirements.txt           # Python dependencies
```

## Requirements

- Python 3.10 or newer
- `pip`

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run commands from the project root with `python main.py`.

Show help:

```bash
python main.py --help
```

Add a user:

```bash
python main.py add-user --name "Alice" --age 30 --email "alice@example.com" --username "alice"
```

List users:

```bash
python main.py list-users
```

Create a project:

```bash
python main.py add-project \
  --title "CLI App" \
  --description "Build a project management command-line app" \
  --start-date "2026-06-01" \
  --end-date "2026-06-30"
```

List projects:

```bash
python main.py list-projects
```

Add a task to a project:

```bash
python main.py add-task \
  --project-id 1 \
  --title "Write tests" \
  --description "Cover the core model behavior"
```

Mark a task as complete:

```bash
python main.py complete-task --project-id 1 --task-id 1
```

## Data Storage

The app stores users, projects, and project tasks in `data/database.json`. The file is loaded when the CLI starts and updated after create or update operations.

## Running Tests

```bash
pytest
```

## Notes

- The app uses only Python standard-library modules at runtime.
- `pytest` is included in `requirements.txt` for running the test suite.
- Because data is saved locally, deleting or replacing `data/database.json` resets the stored users and projects.
