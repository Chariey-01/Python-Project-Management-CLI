# Person class
class Person:
    def __init__(self, name, age, email=None):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        if self.email:
            return f"{self.name}, {self.age} years old, Email: {self.email}"
        return f"{self.name}, {self.age} years old"
# # Example
# if __name__ == "__main__":
#     person1 = Person("Steph", 20, "steph@gmail.com")
#     person2 = Person("Doe", 25, "doe@gmail.com")
#     print(person1)  # Output: Steph, 20 years old, Email: steph@gmail.com
#     print(person2)  # Output: Doe, 25 years old, Email: doe@gmail.com