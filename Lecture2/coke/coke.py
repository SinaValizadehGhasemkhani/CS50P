def main():
    calc()

def calc():
    valid_coins = [25, 10, 5]
    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        user_input = int(input("Insert Coin: "))
        if user_input in valid_coins:
            amount_due -= user_input
        if amount_due <= 0:
            print(f"Change Owed: {amount_due * -1}")

main()
