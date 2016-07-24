class SchoolMember:
    """This is the main class that will be inherited by 2 other child classes"""
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Initialized the school member with name: {}".format(self.name))

    def tell(self):
        print("I am {} who is {} years old".format(self.name,self.age),end="")

class Teacher(SchoolMember):
    """Represents a teacher"""
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print("A teacher has been initialized!")

    def tell(self):
        print("I am a teacher whose name is {} and earning {}".format(self.name,self.salary))

class Student(SchoolMember):
    """Represent a student"""
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks

    def tell(self):
        print("I am a student whose name is {} with {} marks".format(self.name,self.marks))

t = Teacher("Mary", 32, 60000)
s = Student("John", 14, 95)

print()

members = [t,s]
for member in members:
    member.tell()
