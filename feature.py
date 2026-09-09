def calculate_user_discount(user, cart_total): 
    Calculate discount based on user loyalty tier. 
    TODO: finish tier logic, currently only handles 'gold' 
    if user.tier == "gold": 
        discount = cart_total * 0.20 
    elif user.tier == "silver": 
        # TODO: figure out silver discount rate 
        discount = 
    # TODO: handle bronze and new users 
    return discount 
