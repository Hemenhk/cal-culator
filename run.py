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