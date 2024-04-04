"""
https://cs50.harvard.edu/python/2022/psets/1/bank/
"""

def main():
    greet = input("Greeting: ").lower().strip()
    bank(greet)


def bank(n):
    cash = 0
    if (n == 'hello'):
        print(f"${cash}")
    elif (n == 'hello, newman'):
        print(f"${cash}")
    elif (n == 'hey'):
        cash += 20
        print(f"${cash}")
    elif (n == 'How you doing?'):
        cash += 20
        print(f"${cash}")
    elif (n == "what's happening?"):
        cash += 100
        print(f"${cash}")
    elif (n == "what's up?"):
        cash += 100
        print(f"${cash}")
    elif (n == "how's it going?"):
        cash += 20
        print(f"${cash}")

main()
