# Simple Calculator (for addition, subtracton, modulus & Exponential operations)

def add(x, y):
    return x + y  # for Additon

def subtract(x, y):
    return x - y  # for substraction

def mod(x, y):
    return x % y  # for knowing the remainder (Modulus operation)

def exp(x, y):
    return x ** y  # to raise the power

print("Select operation: \n1. Add\n2. Subtract\n3. Modulus operation (to know remainder)\n4. Exponential operation\n")

while True:

    chosen_option = input("Choose from above options(1/2/3/4): ")

    if chosen_option in ('1', '2', '3', '4'):
        n1 = float(input("Enter 1st number: "))
        n2 = float(input("Enter 2nd number: "))

        if chosen_option == '1':
            print(n1, "+", n2, "=", add(n1, n2))

        elif chosen_option == '2':
            print(n1, "-", n2, "=", subtract(n1, n2))

        elif chosen_option == '3':
            print(n1, "%", n2, "=", mod(n1, n2))

        elif chosen_option == '4':
            print(n1, "**", n2, "=", exp(n1, n2))

        another_calculation = input("Will you do another calculation? (yes/no): ")
        if another_calculation == "no":
            break

    else:
        print("Your Choice is not from above options")
