def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    validation = False
    if len(s) > 1 and len(s) < 7:
        start = s[0:2]
        if s.isalpha():
            validation = True
        elif s.isalnum() and start.isalpha():
            if not s[-1].isalpha():
                for character in s[2:]:
                    if character.isalpha():
                        continue
                    elif character.isdigit and character != "0":
                        validation = True
                    break
    return validation



main()
