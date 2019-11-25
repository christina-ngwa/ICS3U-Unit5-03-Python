#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: November 2019
# This program uses return values
# Reference: https://www.w3schools.com/python/python_dictionaries.asp

def convert_grade(grade):
    # list of level of percentages based on the ontario rubric
    ontario_rubric = {}
    ontario_rubric['R-'] = '0%'
    ontario_rubric['R'] = '30%'
    ontario_rubric['R+'] = '40%'
    ontario_rubric['1-'] = '50%'
    ontario_rubric['1'] = '53%'
    ontario_rubric['1+'] = '57%'
    ontario_rubric['2-'] = '60%'
    ontario_rubric['2'] = '63%'
    ontario_rubric['2+'] = '67%'
    ontario_rubric['3-'] = '70%'
    ontario_rubric['3'] = '73%'
    ontario_rubric['3+'] = '77%'
    ontario_rubric['4-'] = '80%'
    ontario_rubric['4'] = '87%'
    ontario_rubric['4+'] = '95%'

    # converts levels to percentages
    if (grade == 'R-' or grade == 'R' or grade == 'R+' or grade == '1-'
            or grade == '1' or grade == '1+' or grade == '2-' or grade == '2'or
            grade == '2+' or grade == '3-' or grade == '3' or grade == '3+'or
            grade == '4-' or grade == '4' or grade == '4+'):
        return ontario_rubric[grade]
    else:
        return -1


def main():
    # input
    print("Welcome to the Ontario Rubric calculator.")
    print("If you received '-1', please try again.")
    print("")
    grade = input("Enter your mark (ex. R+ or 4+): ")
    print("")

    # call functions
    percentage = convert_grade(grade)
    
    # output
    if percentage == -1:
        print("-1")
    else:
        print("You are at a", percentage, ".")


if __name__ == "__main__":
    main()
