"""
https://cs50.harvard.edu/python/2022/psets/1/deep/
"""
def main():
    deep()

def deep():
    n = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
    if n == "42" or n == "forty-two" or n == "forty two":
        print("Yes")

    else :
        print("No")

main()
