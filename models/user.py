from models.person import Person
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


    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "username": self.username,
        }
    
  
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
    
    @property
    def is_admin_user(self):
        return self.is_admin  # Return the value of is_admin to check if the user is an admin

    @is_admin_user.setter
    def is_admin_user(self, value):
        self.is_admin = value  # Set the value of is_admin to make the user an admin or not

    @property
    def email(self):
        return self._email  # Return the email address when accessed

    @email.setter
    def email(self, value):
        if value is None or ("@" in value and "." in value.split("@")[-1]):
            self._email = value  # Set the email if it is valid
        else:
            raise ValueError("Invalid email address")  # Raise an error if the email is invalid

# Override the __str__ method to include username and other user-specific information 
    def __str__(self):
        base_info = super().__str__()
        if self.username:
            return f"{base_info}, Username: {self.username}"
        return base_info
# Example
# if __name__ == "__main__":
#     user1 = User("Jeanne", 19, "jeanne@gmail.com", "jeanne_user")
#     print(user1)  # Output: Jeanne, 19 years old, Email: jeanne@gmail.com, Username: jeanne_user

#     user1.login()  # Simulate user login
#     print(f"Login Attempts: {user1.login_attempts}, Last Login: {user1.last_login}")  # Output: Login Attempts: 1, Last Login: 2024-06-01 12:00:00

#     user1.add_project("Project Quahaston")  
#     print(f"Projects: {user1.projects}")  # Output: Projects: ['Project Quahaston']

#     user1.logout()  # Simulate user logout
#     print(f"Is Active: {user1.is_active}, Last Login: {user1.last_login}, Login Attempts: {user1.login_attempts}, Projects: {user1.projects}")  
#     # Output: Is Active: False, Last Login: None, Login Attempts: 0, Projects: [] 

#     # Example of using the is_admin_user property
#     user1.is_admin_user = True  # Set the user as an admin
#     print(f"Is Admin: {user1.is_admin_user}")  # Output: Is Admin: True

#     # Example of using the email property with validation
#     try:
#         user1.email = "invalid_email"  # attempting to set an invalid email address 
#     except ValueError as e:
#         print(e)  # Output: Invalid email address
#     user1.email = "valid_email@gmail.com"  # Set a valid email address
#     print(f"Email: {user1.email}")  # Output: Email: valid_email@gmail.com
