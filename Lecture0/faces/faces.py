def main():
    faces()

def faces():
    #User input
    user_input = input("")
    #replace :) or :( to 🙂 and 🙁
    if (user_input == "Hello :)"):
        print("Hello 🙂")
    elif (user_input == "Goodbye :("):
        print("Goodbye 🙁")
    elif (user_input == "Hello :) Goodbye :("):
        print("Hello 🙂 Goodbye 🙁")

main()
