def main():
    camelcase = input("camelCase: ")
    print(snake_case(camelcase))

def snake_case(inp):

    return f"snake_case: {''.join(['_' + str(c).lower() if str(c).isupper() else c for c in inp]).lstrip('_')}"

main()
