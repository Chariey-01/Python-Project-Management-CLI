from person import Person
# User class inheriting from Person
class User(Person):
    # Class variable to keep track of user count
    user_counter = 0
    def __init__(self, name, age, email=None, username=None):
        super().__init__(name, age, email)
        self.username = username
        User.user_counter += 1
        self.user_id = User.user_counter
        self.is_active = True  # New attribute to track if the user is active 
        self.is_admin = False  # New attribute to track if the user is an admin 
        self.login_attempts = 0  # New attribute to track login attempts  
        self.last_login = None  # New attribute to track the last login time  
        self.projects = []  # New attribute to track projects associated with the user  

# login method to update login attempts and last login time
    def login(self):
        self.login_attempts += 1
        self.last_login = "2024-06-01 12:00:00"  # Example timestamp for last login 

# logout method to reset login attempts and clear last login time 
    def logout(self):
        self.is_active = False  # Set user as inactive on logout
        self.last_login = None  # Clear the last login time 
        self.login_attempts = 0  # Reset login attempts 
        self.projects = []  # Clear the user's project list 

# method to add a project to the user's project list
    def add_project(self, project_name):
        self.projects.append(project_name)  # Add a project to the user's project list    

# Override the __str__ method to include username and other user-specific information 
    def __str__(self):
        base_info = super().__str__()
        if self.username:
            return f"{base_info}, Username: {self.username}"
        return base_info
# Example
if __name__ == "__main__":
    user1 = User("Jeanne", 19, "jeanne@gmail.com", "jeanne_user")
    print(user1)  # Output: Jeanne, 19 years old, Email: jeanne@gmail.com, Username: jeanne_user