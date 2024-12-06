# output_module.py

def print_and_save_result(operation, num1, num2, result):
    """Function to print the result and save it to a file."""
    if result is not None:
        print(f"The {operation} of {num1} and {num2} is {result}")
        with open("calculations.txt", "a") as file:
            file.write(f"The {operation} of {num1} and {num2} is {result}\n")
