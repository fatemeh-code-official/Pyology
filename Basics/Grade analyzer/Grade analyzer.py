"""
Program: Grade Statistics Analyzer
Author: Fatemeh
Description:
    This program accepts a list of grades (0–20) entered by the user,
    separated by commas. It validates the input to ensure that:
        - The user doesn't skip the input.
        - All entered values are numeric.
        - Only grades within the range [0, 20] are processed.
    
    The program then:
        - Calculates the average of the valid grades.
        - Finds and prints the minimum and maximum grades.
        - Displays all grades greater than the average.
    
    Custom Exceptions:
        - EmptyFieldError: Raised when the user leaves the input blank.
"""


class EmptyFieldError(Exception):
    pass


def calculate_average(grades):
    average = sum(grades)/len(grades)
    return round(average, 2)


def grade_analyzer(grades):
    min_grade = min(grades)
    max_grade = max(grades)
    average = calculate_average(grades)
    print(f"\n\u26A0\ufe0f The minimum grade is {min_grade}")
    print(f"\U0001F3C5 The maximum grade is {max_grade}")
    print(f"\U0001F4CA Your average is {average}")
    above_average = [grade for grade in grades if grade > average]
    print(f"\U0001F4C8 The grades bigger than average => {above_average}")


try:
    user_grades = input(
        "\u2139\ufe0f  Please Enter your grades (0-20) separated by , (like 19.5 , 20) : ").strip()

    if not user_grades:
        raise EmptyFieldError("\u274C You have to enter your grades!")

    grade_list_str = user_grades.split(',')

    grade_list_float = [float(grade)
                        for grade in grade_list_str if grade != '']
    clean_grade_list = [
        grade for grade in grade_list_float if 0 <= grade <= 20]
    if not clean_grade_list:
        raise EmptyFieldError("\u274C All your grades are Invalid!")
    grade_analyzer(clean_grade_list)

except EmptyFieldError as error:
    print(error)
