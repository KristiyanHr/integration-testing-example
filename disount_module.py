def apply_discount(total_price):
    if(total_price > 1000):
        return total_price * 0.9
    elif(total_price > 500 and total_price <= 1000):
        return total_price * 0.95
    elif(total_price < 500):
        return total_price