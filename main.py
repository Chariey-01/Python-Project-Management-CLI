# CLI 
import argparse

from services.project_manager import ProjectManager

manager = ProjectManager()

# parser
parser = argparse.ArgumentParser(
    description="Project Management CLI"
)

subparsers = parser.add_subparsers(dest="command")
# User command
add_user_parser = subparsers.add_parser(
    "add-user",
    help="Add a new user"
)

list_users_parser = subparsers.add_parser(
    "list-users",
    help="Display all users"
)

list_projects_parser = subparsers.add_parser(
    "list-projects",
    help="Display all projects"
)
add_user_parser.add_argument("--name", required=True)
add_user_parser.add_argument("--age", type=int, required=True)
add_user_parser.add_argument("--email")
add_user_parser.add_argument("--username")

# Arguments Processing
args = parser.parse_args()

if args.command == "add-user":
    try:
        manager.create_user(
            args.name,
            args.age,
            args.email,
            args.username
        )
    except ValueError as error:
        parser.error(str(error))

    print("User added successfully")


elif args.command == "list-users":

    users = manager.get_all_users()

    if not users:
        print("No users found")

    for user in users:
        print(user)

elif args.command == "add-project":

    manager.create_project(
        args.title,
        args.description,
        args.start_date,
        args.end_date
    )

    print("Project added successfully")

elif args.command == "list-projects":

    projects = manager.get_all_projects()

    if not projects:
        print("No projects found")

    for project in projects:
        print(project)   

elif args.command == "complete-task":

    success = manager.complete_task(
        args.project_id,
        args.task_id
    )

    if success:
        print("Task completed")
    else:
        print("Task not found")

else:
    parser.print_help()
# Add project comand
add_project_parser = subparsers.add_parser(
    "add-project",
    help="Create a project"
)

add_project_parser.add_argument(
    "--title",
    required=True
)

add_project_parser.add_argument(
    "--description",
    required=True
)

add_project_parser.add_argument(
    "--start-date",
    required=True
)

add_project_parser.add_argument(
    "--end-date",
    required=True
)
# Add task command
add_task_parser = subparsers.add_parser(
    "add-task",
    help="Add task to project"
)

add_task_parser.add_argument(
    "--project-id",
    type=int,
    required=True
)

add_task_parser.add_argument(
    "--title",
    required=True
)

add_task_parser.add_argument(
    "--description",
    required=True
)
# Complete task command
complete_task_parser = subparsers.add_parser(
    "complete-task"
)

complete_task_parser.add_argument(
    "--project-id",
    type=int,
    required=True
)

complete_task_parser.add_argument(
    "--task-id",
    type=int,
    required=True
)
