import gspread
from google.oauth2.service_account import Credentials
from bmr import (age, height, weight)


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('user_bmr')


def main():
    """
    This is the main function that calculates the BMR
    of either a male or a female user.

    At the end of the function a list will be generated
    which will then be uploaded and stored in a Google
    spreadsheet
    """

    print("Welcome to CalCulator\n")

    print("""On this app you'll acquire your Basal Metabolic Rate (BMR).
By typing in personal values of your height, age, weight and gender,
we will calculate your BMR so that you can either increase your calories
to build muscle, or to decrease your calories to burn fat.

In the end you'll be given a list,
of which to store your results in a Google Spreadsheet.\n""")

    print("All values entered must be numeric values such as '1', '72' '23'\n")

    user_list = []
    try:
        age_input = float(input("What's your age in years?:\n "))
        print(f"\nYou are {age_input} years old\n")
        user_list.append(age_input)

        height_input = float(input("What's your height in cm?:\n "))
        print(f"\nYou are {height_input} cm tall\n")
        user_list.append(height_input)

        weight_input = float(input("What's your weight in kg?:\n"))
        print(f"\nYou weigh {weight_input} kg\n")
        user_list.append(weight_input)

        print("""If you are male enter '1'.
If you are female enter any other numeric value: \n """)
        gender = int(input("What is your gender?:\n "))
    except ValueError:
        print("Invalid value. You must type a numeric value")

    print("\nCalculating your BMR, rounded to the closest int...\n ")

    if gender == 1:
        bmr = round(88.362 + weight.weight_men_bmr(weight_input) +
                    height.height_men_bmr(height_input) -
                    age.age_men_bmr(age_input))
    else:
        bmr = round(447.593 + weight.weight_women_bmr(weight_input) +
                    height.height_women_bmr(height_input) -
                    age.age_women_bmr(age_input))
    print(f"Your BMR is {bmr} calories\n ")
    user_list.append(bmr)

    print(user_list)
    print("\nCalculation finished.\n")

    """
    These four lines of code (line 77-80) are used
    to update the worksheet.
    """

    # These lines of code are credited to Anna Greaves' Love Sandwiches
    print("Updating bmr_outpt worksheet...\n")
    bmr_outpt_worksheet = SHEET.worksheet("bmr_outpt")
    bmr_outpt_worksheet.append_row(user_list)
    print("Bmr_outpt worksheet updated successfully.\n")

    return bmr


main()
print("\nThank you for using CalCulator!\n")
