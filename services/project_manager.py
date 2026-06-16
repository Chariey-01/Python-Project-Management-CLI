from models.projects import Project
from models.user import User
from models.task import Task
from utils.file_handler import save_data
from utils.file_handler import load_data
from datetime import date, datetime

class ProjectManager:
    def __init__(self):
        self.projects = []  # List to store all projects
        self.users = []     #List of all users
    def create_project(self, title, description, start_date, end_date):
        project = Project(title, description, start_date, end_date)  # Create a new project instance
        self.projects.append(project)  # Add the project to the list of projects
        self.save_to_file()
        return project  # Return the created project

    def get_project_by_id(self, project_id):
        for project in self.projects:  # Iterate through the list of projects
            if project.project_id == project_id:  # Check if the project ID matches
                return project  # Return the matching project
        return None  # Return None if no matching project is found

    def assign_task_to_project(self, project_id, task):
        project = self.get_project_by_id(project_id)  # Get the project by ID
        if project:  # Check if the project exists
            project.add_task(task)  # Add the task to the project's task list
            self.save_to_file()
            return True  # Return True if the task was successfully assigned
        return False  # Return False if the project was not found
# Example usage
# if __name__ == "__main__":
#     project_manager = ProjectManager()  # Create an instance of ProjectManager
#     project1 = project_manager.create_project("New Website", "Develop a new company website.", "2024-06-01", "2024-12-31")  # Create a new project
#     print(project1)  # Output: Project ID: 1, Name: New Website, Description: Develop a new company website., Start Date: 2024-06-01, End Date: 2024-12-31

#     task1 = Task("Design Homepage", "Create a design for the homepage of the website.")  # Create a new task
#     project_manager.assign_task_to_project(project1.project_id, task1)  # Assign the task to the project
#     print(project1.tasks[0])  # Output: Task ID: 1, Title: Design Homepage, Description: Create a design for the homepage of the website., Assigned To: Unassigned, Status: Not Started

    def get_all_projects(self):
        return self.projects  # Return the list of all projects   

    def remove_project(self, project_id):
        project = self.get_project_by_id(project_id)  # Get the project by ID
        if project:  # Check if the project exists
            self.projects.remove(project)  # Remove the project from the list of projects
            return True  # Return True if the project was successfully removed
        return False  # Return False if the project was not found
# example usage of additional methods
# if __name__ == "__main__":  
#      project_manager = ProjectManager()  # Create an instance of ProjectManager
# project1 = project_manager.create_project("New Website", "Develop a new company website.", "2024-06-01", "2024-12-31")  # Create a new project
    
    def create_user(self, name, age, email=None, username=None):
        user = User(name, age, email, username)
        self.users.append(user)
        self.save_to_file()
        return user

    def update_project(self, project_id, title=None, description=None, start_date=None, end_date=None):
        project = self.get_project_by_id(project_id)  # Get the project by ID
        if project:  # Check if the project exists
            if title:  # Update the title if provided
                project.name = title
            if description:  # Update the description if provided
                project.description = description
            if start_date:  # Update the start date if provided
                project.start_date = start_date
            if end_date:  # Update the end date if provided
                project.end_date = end_date
            return True  # Return True if the project was successfully updated
        return False  # Return False if the project was not found

    def get_tasks_for_project(self, project_id):
        project = self.get_project_by_id(project_id)  # Get the project by ID
        if project:  # Check if the project exists
            return project.tasks  # Return the list of tasks associated with the project
        return None  # Return None if the project was not found 

    def get_projects_for_user(self, user):
        user_projects = []  # List to store projects associated with the user
        for project in self.projects:  # Iterate through the list of projects
            assigned_to_task = user.username in [
                task.assigned_to.username for task in project.tasks if task.assigned_to
            ]
            listed_on_user = project.name in user.projects
            if assigned_to_task or listed_on_user:
                user_projects.append(project)  # Add the project to the user's project list if they are assigned to a task
        return user_projects  # Return the list of projects associated with the user

    def get_users_for_project(self, project_id):
        project = self.get_project_by_id(project_id)  # Get the project by ID
        if project:  # Check if the project exists
            users = set()  # Use a set to avoid duplicate users
            for task in project.tasks:  # Iterate through the tasks in the project
                if task.assigned_to:  # Check if the task is assigned to a user
                    users.add(task.assigned_to)  # Add the assigned user to the set of users
            return list(users)  # Return the list of unique users associated with the project
        return None  # Return None if the project was not found

    def get_overdue_tasks(self, project_id):
        project = self.get_project_by_id(project_id)  # Get the project by ID
        if project:  # Check if the project exists
            overdue_tasks = []  # List to store overdue tasks
            for task in project.tasks:  # Iterate through the tasks in the project
                if task.due_date and self._parse_due_date(task.due_date) < date.today():
                    overdue_tasks.append(task)  # Add the overdue task to the list of overdue tasks
            return overdue_tasks  # Return the list of overdue tasks
        return None  # Return None if the project was not found

    @staticmethod
    def _parse_due_date(due_date):
        if isinstance(due_date, datetime):
            return due_date.date()
        if isinstance(due_date, date):
            return due_date
        return datetime.strptime(due_date, "%Y-%m-%d").date()

    def get_completed_tasks(self, project_id):
        project = self.get_project_by_id(project_id)  # Get the project by ID
        if project:  # Check elf.save_to_file()if the project exists
            completed_tasks = [task for task in project.tasks if task.is_complete]  # List comprehension to get completed tasks
            self.save_to_file()
            return completed_tasks  # Return the list of completed tasks
        return None  # Return None if the project was not found

    def get_incomplete_tasks(self, project_id):
        project = self.get_project_by_id(project_id)  # Get the project by ID
        if project:  # Check if the project exists
            incomplete_tasks = [task for task in project.tasks if not task.is_complete]  # List comprehension to get incomplete tasks
            return incomplete_tasks  # Return the list of incomplete tasks
        return None  # Return None if the project was not found

    def get_tasks_by_status(self, project_id, status):
        project = self.get_project_by_id(project_id)  # Get the project by ID
        if project:  # Check if the project exists
            tasks_by_status = [task for task in project.tasks if task.status == status]  # List comprehension to get tasks by status
            return tasks_by_status  # Return the list of tasks with the specified status
        return None  # Return None if the project was not found

    def get_tasks_by_user(self, project_id, user):
        project = self.get_project_by_id(project_id)  # Get the project by ID
        if project:  # Check if the project exists
            tasks_by_user = [task for task in project.tasks if task.assigned_to and task.assigned_to.username == user.username]  # List comprehension to get tasks assigned to the specified user
            return tasks_by_user  # Return the list of tasks assigned to the user
        return None  # Return None if the project was not found

    def add_user_to_project(self, project_id, user):
        project = self.get_project_by_id(project_id)  # Get the project by ID
        if project:  # Check if the project exists
            for task in project.tasks:  # Iterate through the tasks in the project
                if task.assigned_to and task.assigned_to.username == user.username:  # Check if the user is already assigned to a task in the project
                    return False  # Return False if the user is already assigned to a task in the project
            user.add_project(project.name)  # Add the project to the user's project list
            return True  # Return True if the user was successfully added to the project
        return False  # Return False if the project was not found

    def remove_user_from_project(self, project_id, user):
        project = self.get_project_by_id(project_id)  # Get the project by ID
        if project:  # Check if the project exists
            for task in project.tasks:  # Iterate through the tasks in the project
                if task.assigned_to and task.assigned_to.username == user.username:  # Check if the user is assigned to a task in the project
                    task.assigned_to = None  # Unassign the user from the task
            if project.name in user.projects:  # Check if the project is in the user's project list
                user.projects.remove(project.name)  # Remove the project from the user's project list
            return True  # Return True if the user was successfully removed from the project
        return False  # Return False if the project was not found
    def get_project_summary(self, project_id):
        project = self.get_project_by_id(project_id)  # Get the project by ID
        if project:  # Check if the project exists
            summary = {
                "Project Name": project.name,
                "Description": project.description,
                "Start Date": project.start_date,
                "End Date": project.end_date,
                "Total Tasks": len(project.tasks),
                "Completed Tasks": len([task for task in project.tasks if task.is_complete]),
                "Incomplete Tasks": len([task for task in project.tasks if not task.is_complete]),
            }
            return summary  # Return the project summary as a dictionary
        return None  # Return None if the project was not found
    def get_user_summary(self, user):
        user_projects = self.get_projects_for_user(user)  # Get the projects associated with the user
        summary = {
            "Username": user.username,
            "Email": user.email,
            "Total Projects": len(user_projects),
            "Projects": [project.name for project in user_projects],  # List of project names associated with the user
        }
        return summary  # Return the user summary as a dictionary

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

#   Example usage of additional methods
# if __name__ == "__main__":    project_manager = ProjectManager()  # Create an instance of ProjectManager
# user1 = User("Jeanne", 19, "jeanne@gmail.com") # Create a new user
# project1 = project_manager.create_project("New Website", "Develop a new company website.", "2024-06-01", "2024-12-31")  # Create a new project
# task1 = Task("Design Homepage", "Create a design for the homepage of the website.")  # Create a new task
# project_manager.assign_task_to_project(project1.project_id, task1)  # Assign the task to the project
# project_manager.add_user_to_project(project1.project_id, user1)  # Add the user to the project
# print(project_manager.get_project_summary(project1.project_id))  
# print(project_manager.get_user_summary(user1))  
    def save_to_file(self):
        data = {
            "users": [user.to_dict() for user in self.users],
            "projects": [project.to_dict() for project in self.projects],
        }
        save_data(data)

    def load_from_file(self):
        data = load_data()
        return data
