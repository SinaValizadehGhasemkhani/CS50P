def main():
    user_input = input("Input: ")

    print(omitted(user_input))

def omitted(str_to_vowel):
    vowels = ['a', 'e', 'i', 'o', 'u']
    no_vowels = ""
    for character in str_to_vowel:
        if character.lower() not in vowels:
            no_vowels += character

    return no_vowels

main()
