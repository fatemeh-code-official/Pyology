"""
Program: Password Strength Analyzer
Author: Fatemeh
Description:
    This program analyzes the strength of a user-submitted password based on
    standard security rules. It evaluates the password by checking:
        - Total length
        - Presence of lowercase letters
        - Presence of uppercase letters
        - Presence of digits
        - Presence of punctuation symbols

    The password is classified into one of the following categories:
        - Weak:
            length < 8
        - Medium:
            length >= 8 AND contains at least 2 different character types
        - Strong:
            length >= 10 AND contains at least 3 different character types
        - Very Strong:
            length >= 12 AND contains all 4 character types
              (digits, lowercase, uppercase, punctuation)

    Functional Overview:
        1. The program checks for empty input.
        2. It removes whitespace characters from the password.
        3. It counts the occurrence of each character category.
        4. It determines the number of unique character types in the password.
        5. Based on predefined rules, it prints the final strength result.

    Custom Exceptions:
        - EmptyFieldError:
            Raised when the user enters an empty password.
        - ShortLenError:
            Raised when the password length is below the minimum acceptable
            size for analysis.

    Notes:
        - Unicode symbol codes (e.g., \u274C, \u26A0, \u2705, \U0001F4AA)
          are used to display strength messages instead of emoji characters.
"""

import string


class EmptyFieldError(Exception):
    pass


class ShortLenError(Exception):
    pass


# A function that analyze the paramters of password and return them

def analyze_password(password_list):
    digits = sum(char.isdigit() for char in password_list)
    lowers = sum(char.islower() for char in password_list)
    uppers = sum(char.isupper() for char in password_list)
    puncts = sum(char in string.punctuation for char in password_list)
    length = len(password_list)

    types = 0
    if digits > 0: types += 1
    if lowers > 0: types += 1
    if uppers > 0: types += 1
    if puncts > 0: types += 1

    return digits, lowers, uppers, puncts, types, length


# A funtion that validates the quality of password

def validate_password():
    digits, lowers, uppers, puncts, types, length = analyze_password(password_list)

    if length >= 12 and types == 4:
        print("\U0001F4AA  Very Strong Password")

    elif length >= 10 and types >= 3:
        print("\u2705  Strong Password")

    elif length >= 8 and types >= 2:
        print("\u26A0\ufe0f  Medium Password")

    elif length < 8:
        print("\u274C  Weak Password")


try:
    password = input("Please enter your password : ").strip()
    if not password:
        raise EmptyFieldError("\u26A0\ufe0f   You have to enter something")

    password_list = [char for char in password if not char.isspace()]
    if len(password_list) < 5:
        raise ShortLenError(
            "You\u26A0\ufe0f   You have to enter a password contains atleast 5 characters")

    validate_password()
except (EmptyFieldError, ShortLenError) as e:
    print(e)
