def main():
    user_input()


def user_input():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x = float(x)
    z = float(z)
    math_interpreter(x, y, z)
    
def math_interpreter(a, b, c):
    if b == "+":
        print(f"{a+c:0.1f}")
    elif b == "-":
        print(f"{a-c:0.1f}")
    elif b == "*":
        print(f"{a*c:0.1f}")
    elif b == "/":
        print(f"{a/c:0.1f}")


main()
