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

add_user_parser.add_argument("--name", required=True)
add_user_parser.add_argument("--age", type=int, required=True)
add_user_parser.add_argument("--email")
add_user_parser.add_argument("--username")

# Arguments Processing
args = parser.parse_args()

if args.command == "add-user":

    manager.create_user(
        args.name,
        args.age,
        args.email,
        args.username
    )

    print("User added successfully")

    