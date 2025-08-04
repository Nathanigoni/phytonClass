def apply_discount(amount):
    if amount > 500:
        discount = 0.20
    elif amount > 100:
        discount = 0.10
    else:
        discount = 0.0

    final_amount = amount - (amount * discount)
    return final_amount
print(apply_discount(801)) 