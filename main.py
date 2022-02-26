import random
from src.student import Student
from src.roster import Roster


##############################
###     Jaylon Ignacio     ###
###    "Assign Students    ###
###          to a          ###
###       Discussion"      ###
##############################

# Need a class for student which will have first and last name and also a variable for the names of
# the people they have been assigned to and a variable for the number of people assigned to them
# Have a list initially iterate and create each student as an object through a for loop
# Attribute for Student should be to assign themselves to someone else which also adds 1 to the parameter num_assigned of the person they are assigned to
# Generate max_students number of numbers in a list where each number can only be used once

# How do I get information from 10th student from my Roster that comes from the list


def main():

    list_of_students = ["Braylen Ghost", "Kadin Bobby", "Eddie Debbie", "Jaeden John", "Andreas Lexy",
                        "Brayan Bobby", "Adrian Digs", "Byron Max", "Derrick Brown", "Trevin Andre", "Joshua Ticks", "Dario Luigi", "John Lane", "Alberto Gutierrez"]

    Rucker = Roster("English", len(list_of_students))

    assigned_one = [random.sample(
        range(Rucker.max_students), Rucker.max_students)]
    assigned_two = [random.sample(
        range(Rucker.max_students), Rucker.max_students)]

    #first_assigned, second_assigned = list_of_students[assigned_one[0][0]]

    for x in range(Rucker.max_students):
        first, last = list_of_students[x].split()
        first_assigned = list_of_students[assigned_one[0][x]]
        second_assigned = list_of_students[assigned_two[0][x]]

        Rucker.add_students(
            Student(first, last, first_assigned, second_assigned))

    r_string = f'\t\tHere is the list of your {Rucker.max_students} students and who they are assigned to.\n'
    for k in range(Rucker.max_students):
        r_string += f'\t{Rucker.students[k].first_name} {Rucker.students[k].last_name}: {Rucker.students[k].assigned1} and {Rucker.students[k].assigned2}\n'

    print(r_string)


if __name__ == "__main__":
    main()
