# Project class
class Project:
    # Class variable to keep track of project IDs
    project_id_counter = 1

    def __init__(self, title, description, start_date, end_date):
        self.project_id = Project.project_id_counter
        Project.project_id_counter += 1  # Increment the project ID counter for the next project
        self.name = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []  # New attribute to track tasks associated with the project  

    def to_dict(self):
        return {
            "project_id": self.project_id,
            "title": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "tasks":[task.to_dict() for task in self.tasks]
        }
    # Method to add a task to the project's task list
    def add_task(self, task):
        self.tasks.append(task)  # Add a task to the project's task list  
        
     # Override the __str__ method to provide a string representation of the project    
    def __str__(self):
        return f"Project ID: {self.project_id}, Name: {self.name}, Description: {self.description}, Start Date: {self.start_date}, End Date: {self.end_date}"
# Example
# if __name__ == "__main__":
#     project1 = Project("Website Mockup", "Create a mockup of the new website design.", "2024-06-01", "2024-12-31")
#     print(project1) 
