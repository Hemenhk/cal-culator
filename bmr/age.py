def age_men_bmr(age):
    """
    This function calculates the age variable
    which is going to be used in calculating
    the male user's bmr
    """
    # print("This is your age variable used in calculating your bmr\n ")
    ages_bmr_men = age * 5.677
    return ages_bmr_men


def age_women_bmr(age):
    """
    This function calculates the age variable
    which is going to be used in calculating
    the female user's bmr
    """
    # print("This is your age variable used in calculating your bmr\n ")
    ages_bmr_women = age * 4.33
    return ages_bmr_women
