from weight import weight_men_bmr, weight_women_bmr
from height import height_men_bmr, height_women_bmr
from age import age_men_bmr, age_women_bmr


def main():
    """
    This is the main function that calculates the bmr
    of either a male or female user."""

    print("Welcome to CalCulator")

    print("""On this app you'll be able to find your Basal Metabolic Rate, or BMR.
By typing in personal values of your height, age, weight and gender,
we will calculate your BMR so that you can either increase your calories
to build muscle, or to decrease your calories to burn fat.\n""")

    print("All values entered must be numeric values such as '1', '2' '3'\n")

    try:
        age = float(input("What's your age in years?:\n "))
        print(f"You are {age} years old\n")

        height = float(input("What's your height in cm?:\n "))
        print(f"You are {height} cm tall\n")

        weight = float(input("What's your weight in kg?:\n"))
        print(f"You weigh {weight} kg\n")

        print("""If you are male enter '1'.
If you are female enter any other numeric value: \n """)
        gender = int(input("What is your gender?:\n "))
    except ValueError:
        print("Invalid value. You must type a numeric value")

    print("Calculating your bmr, rounded to the closest int...\n ")

    if gender == 1:
        bmr = round(88.362 + weight_men_bmr(weight) + height_men_bmr(height) - age_men_bmr(age))
    else:
        bmr = round(447.593 + weight_women_bmr(weight) + height_women_bmr(height) - age_women_bmr(age))
    print(f"Your bmr is {bmr} calories\n ")

    print("Calculation finished.")

main()
