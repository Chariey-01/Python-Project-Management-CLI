from datetime import datetime

# Task class
class Task:
    # Class variable to keep track of task IDs
    task_id_counter = 0
    def __init__(self, title, description, assigned_to=None):
        
        self.task_id = Task.task_id_counter + 1  # Assign a unique task ID
        Task.task_id_counter += 1  # Increment the task ID counter for the next task  
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.created_at = datetime.now()  
        self.updated_at = datetime.now() # Initialize updated_at with the same timestamp as created_at  
        self.due_date = None  # New attribute to track the due date of the task 
        self.status = "Not Started"  # New attribute to track the status of the task  
        self.is_complete = False


    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "is_complete": self.is_complete,
        }

    # Method to update the task status and set is_complete to True if the task is marked as complete
    def update_status(self, new_status):
        self.status = new_status
        self.updated_at = datetime.now()
        self.is_complete = new_status == "Complete"
    # Method to assign the task to a user
    def assign_to(self, user):
        self.assigned_to = user # Assign the task to a user and update the updated_at timestamp 
        self.updated_at = datetime.now()
    # Override the __str__ method to provide a string representation of the task
    def __str__(self):
        assigned_user = self.assigned_to.username if self.assigned_to else "Unassigned"
        return f"Task ID: {self.task_id}, Title: {self.title}, Description: {self.description}, Assigned To: {assigned_user}, Status: {self.status}"  
# Example
# if __name__ == "__main__":  
#     task1 = Task("Design Homepage", "Create a design for the homepage of the website.")
#     print(task1)  # Output: Task ID: 1, Title: Design Homepage, Description: Create a design for the homepage of the website., Assigned To: Unassigned, Status: Not Started
#     task1.update_status("In Progress")
#     print(task1)  # Output: Task ID: 1, Title: Design Homepage, Description: Create a design for the homepage of the website., Assigned To: Unassigned, Status: In Progress
#     task1.update_status("Complete")
#     print(task1)  # Output: Task ID: 1, Title: Design Homepage, Description: Create a design for the homepage of the website., Assigned To: Unassigned, Status: Complete
