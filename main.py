from art import logo
print(logo)

# my_favourite_operation = add
# my_favourite_operation(2, 5)
# print(mathematical_operations["*"](4,8))

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

mathematical_operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    n1 = float(input("What's the first number?: "))
    continue_calc = True

    while continue_calc:
        operation = input("+\n-\n*\n/\nPick an operation: ")
        n2 = float(input("What's the next number?: "))
        result = mathematical_operations[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {result}")

        next_operation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if next_operation == "y":
            n1 = result
        else:
            continue_calc = False
            print("\n" *20)
            calculator()
calculator()
