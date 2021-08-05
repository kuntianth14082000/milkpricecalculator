def BUFFALO(quantity,fat):
    if fat<2:
        price = quantity * 40
    elif fat>2 and fat<4:
        price = quantity * 42
    elif fat>=4 and fat<6:
        price = quantity * 44
    elif fat>=6 and fat<8:
        price = quantity * 46
    elif fat>=8 and fat<10:
        price = quantity * 48
    elif fat>10:
        price=quantity*50
    else :
        price=0

    return price