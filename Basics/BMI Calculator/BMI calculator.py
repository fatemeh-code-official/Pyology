"""
Program: BMI (Body Mass Index) Calculator
Author: Fatemeh
Description:
    This program calculates the user's Body Mass Index (BMI) based on
    their weight (in kilograms) and height (in meters). It validates
    user input, handles invalid or missing values gracefully, and classifies
    the BMI result into one of the standard categories:
        - Underweight: BMI < 18.5
        - Normal weight: 18.5 <= BMI < 25
        - Overweight: 25 <= BMI < 30
        - Obese: BMI >= 30
"""

class EmptyFieldError(Exception):
    """Raised when one or more input fields are left empty."""
    pass


def bmi_calculator(weight, height):
    """Calculates and returns the BMI rounded to two decimals."""
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def bmi_analyzer(bmi):
    """Analyzes the BMI value and prints the health category."""
    if bmi < 18.5:
        print(f"Your BMI is {bmi} — Underweight \u26A0")
    elif 18.5 <= bmi < 25:
        print(f"Your BMI is {bmi} — Normal weight \u2705")
    elif 25 <= bmi < 30:
        print(f"Your BMI is {bmi} — Overweight \u26A0")
    else:
        print(f"Your BMI is {bmi} — Obese \U0001F6A8")


try:
    weight_input = input("Please enter your weight (kg): ").strip()
    height_input = input("Please enter your height (m, e.g. 1.75): ").strip()

    # Check for empty input
    if not weight_input or not height_input:
        raise EmptyFieldError("\u274C Please do not skip blank fields.")

    # Convert to float
    weight = float(weight_input)
    height = float(height_input)

    # Validate logical values
    if weight <= 0 or height <= 0:
        raise ValueError("\u26A0 Height and weight must be greater than zero.")

    # Run BMI process
    bmi_value = bmi_calculator(weight, height)
    bmi_analyzer(bmi_value)

# === Error Handling ===
except EmptyFieldError as e:
    print(e)
except ValueError as e:
    print(f"Invalid input: {e}")
except Exception as e:
    print(f"Unexpected error occurred: {e}")
