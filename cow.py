def cow(quantity,fat):
    if fat < 2:
        price = quantity * 28
    elif fat > 2 and fat < 4:
        price = quantity * 30
    elif fat >= 4 and fat < 6:
        price = quantity * 32
    elif fat >= 6 and fat < 8:
        price = quantity * 34
    elif fat >= 8 and fat < 10:
        price = quantity * 36
    elif fat > 10:
        price = quantity * 38
    else:
        price = 0

    return price