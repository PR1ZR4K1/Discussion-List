import random
from src.student import Student
from src.roster import Roster
from time import time

start = time()

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

# a = {
#     "j": {
#         "Responded To": ["John", "Christian"],
#     }
# }

# print(a["j"]["Responded To"])  # -> ["John", "Christian"]


def main():

    list_of_students = ["Ashton Holly", "Brielle Monroe", "Gael Elsher", "Evan Gonzalez", "Iris Robinson", "Zoe Brown", "Landon Jones", "Brandon Hernandez", "Olivia Levine", "Jesse Baker",
                        "Camden Hall", "Jackson Martinez", "Elias May", "Harper West", "Juliette Ellis", "Violet Flores", "Beckham Brown", "Charles Ellis", "Knox Sharpe"]

    Rucker = Roster("English", len(list_of_students))

    wrong = True
    count_tries = 0

    while (wrong):
        repeat = 0
        count_tries += 1

        assigned_one = [random.sample(
            range(Rucker.max_students), Rucker.max_students)]
        assigned_two = [random.sample(
            range(Rucker.max_students), Rucker.max_students)]
        for x in range(Rucker.max_students):
            if (assigned_two[0][x] == assigned_one[0][x] or assigned_one[0][x] == x or assigned_two[0][x] == x):
                repeat += 1

        if (repeat == 0):
            wrong = False

    for x in range(Rucker.max_students):
        name = list_of_students[x]
        first_assigned = list_of_students[assigned_one[0][x]]
        second_assigned = list_of_students[assigned_two[0][x]]

        Rucker.add_students(
            Student(name, first_assigned, second_assigned))

    r_string = f'It took {count_tries} tries to retrieve this data, but...\n'
    r_string += f'\t\tHere is the list of your {Rucker.max_students} students and who they are assigned to.\n\n'
    for k in range(Rucker.max_students):
        r_string += f'\t{Rucker.students[k].name}: {Rucker.students[k].assigned1}, {Rucker.students[k].assigned2}\n\n'

    print(r_string)


if __name__ == "__main__":
    main()

# end = time()
# print(end-start)
