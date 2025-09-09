class Student:
    def __init__(self, name, roll, grade):
        self.name = name
        self.roll = roll
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Roll: {self.roll}, Grade: {self.grade}")

s1 = Student("Cristiano", 7, "GOAT")
s1.display_info()
