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


def input_with_validation(input_message, validation_rule=None,
                          error_message="Please enter a valid value"):
    """
    Input value from standard input and validates that
    the value is a valid integer value.
    """
    value = None
    valid_input = False
    while not valid_input:
        input_value = input(input_message)
        try:
            value = int(input_value)
            if validation_rule is not None:
                valid_input = validation_rule(value)
                if not valid_input:
                    print(f"{error_message}\n")
            else:
                valid_input = True
        except ValueError:
            print("Invalid value. You must type a numeric value")
            valid_input = False
    return value


def add_row_to_spreadsheet(row):
    """ Add result to the Google Spreadsheet
    """
    # These lines of code are credited to Anna Greaves' Love Sandwiches
    print("Updating bmr_outpt worksheet...\n")
    bmr_outpt_worksheet = SHEET.worksheet("bmr_outpt")
    bmr_outpt_worksheet.append_row(row)
    print("Bmr_outpt worksheet updated successfully.\n")


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

    age_input = input_with_validation("What's your age in years?: ",
                                      lambda x: 0 < x <= 120,
                                      "The value must be between [1..120]")
    print(f"\nYou are {age_input} years old\n")
    user_list.append(age_input)

    height_input = input_with_validation("What's your height in cm?: ",
                                         lambda x: 0 < x <= 250,
                                         "The value must be between [1..250]")
    print(f"\nYou are {height_input} cm tall\n")
    user_list.append(height_input)

    weight_input = input_with_validation("What's your weight in kg?: ",
                                         lambda x: 0 < x <= 300,
                                         "The value must be between [1..300]")
    print(f"\nYou weigh {weight_input} kg\n")
    user_list.append(weight_input)

    gender = input_with_validation(
        "Gender: enter '1' for male or '2' for female: ",
        lambda x: x in [1, 2])
    print("\nCalculating your BMR, rounded to the closest int...\n")

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

    add_row_to_spreadsheet(user_list)


main()
print("\nThank you for using CalCulator!\n")
