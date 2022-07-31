from weight import weight_men_bmr
from weight import weight_women_bmr
from height import height_men_bmr
from height import height_women_bmr


def main():
    """
    This is the main function that calculates the bmr
    of either a male or female user. 
    """

    try:
        age = float(input("what's your age in years?:\n "))
        print(f"you are {age} years old\n")

        height = float(input("what's your height in cm?:\n "))
        print(f"you are {height} cm tall\n")

        weight = float(input("what's your weight in kg?:\n"))
        print(f"you weigh {weight} kg\n")

        print("if you are male enter '1', if you are female enter any other value: \n ")
        gender = int(input("What is your gender?:\n "))
    except ValueError:
        print("Invalid value. You must type a numeric value")