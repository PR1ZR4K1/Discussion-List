from src.student import Student

##############################
###     Jaylon Ignacio     ###
###    "Assign Students    ###
###          to a          ###
###       Discussion"      ###
##############################

# Need a class for the roster which will have a list of all the students in a certain course


class Roster():
    def __init__(self, course: str, max_students: int) -> None:
        self.course = course
        self.max_students = max_students
        self.students = []

    def add_students(self, student: Student) -> None:
        if len(self.students) < self.max_students:
            self.students.append(student)
        return False

    def assign_student(self, student: Student) -> None:
        print("Nice")
