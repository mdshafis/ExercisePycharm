def pizzaPurchase():
    pizza1 = float(input("Enter the pizza price 1: "))
    pizza2 = float(input("Enter the pizza price 2: "))
    pd1 = float(input("Enter the pizza diameter 1: "))
    pd2 = float(input("Enter the pizza diameter 2: "))

    area1 = (3.14 / 4) * pd1 ** 2
    area2 = (3.14 / 4) * pd2 ** 2

    price1 = pizza1 / area1
    price2 = pizza2 / area2

    if price1 > price2:
        print(f"You sould purchase pizza 2 bcz it is {price2:.2f} per sqr mtr.")
    elif price2 > price1:
        print(f"You sould purchase pizza 1 bcz it is {price1:.2f} per sqr mtr.")


pizzaPurchase()