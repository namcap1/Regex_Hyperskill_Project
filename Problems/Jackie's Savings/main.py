def final_deposit_amount(*interest, amount=1000):
    for i in interest:
        add = amount * (i/100)
        amount += add
    return round(amount, 2)
