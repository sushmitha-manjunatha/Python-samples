def add(a, b):
    """
    Add two numbers.

    Parameters
    ----------
    a : float or int
        The first operand.
    b : float or int
        The second operand.

    Returns
    -------
    float or int
        The sum of a and b.
    """
    return a + b


def subtract(a, b):
    """
    Subtract one number from another.

    Parameters
    ----------
    a : float or int
        The value to subtract from (minuend).
    b : float or int
        The value to subtract (subtrahend).

    Returns
    -------
    float or int
        The result of a - b.
    """
    return a - b


def main():
    """
    Run a simple command-line calculator.

    This function prompts the user to choose an operation (add or subtract),
    collects two numeric inputs, calls the appropriate function, and prints
    the result to the console.
    """
    print("Simple Calculator - Add and Subtract")
    print("1. Add")
    print("2. Subtract")

    choice = input("Choose an option (1 or 2): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == "2":
        result = subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
