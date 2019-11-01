class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
        print(f"Student's name {self.name} Age {self.age}: 23, Major: {self.major}")

steve = Student('Steven Schultz', '23', 'English')
johnny = Student("Jonathan Rosenberg", 24, "Biology")
penny = Student("Penelope Meramveliotakis", 21, "Physics")
