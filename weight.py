def weight_men_bmr(weight):
    """
    This function calculates the weight variable
    which is going to be used in calculating
    the male user's bmr
    """
    #print("This is your weight variable used in calculating your bmr\n ")
    
    weights_bmr_men = weight * 13.397
    return weights_bmr_men

def weight_women_bmr(weight):
    """
    This function calculates the weight variable
    which is going to be used in calculating
    the female user's bmr
    """
    #print("This is your weight variable used in calculating your bmr\n ")
    
    weights_bmr_women = weight * 9.247
    return weights_bmr_women