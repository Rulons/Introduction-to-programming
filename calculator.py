# calculator.py

from modules.input_module import get_numbers
from modules.processing_module import add, subtract, multiply, divide
from modules.output_module import print_and_save_result

def main():
    num1, num2 = get_numbers()
    if num1 is None or num2 is None:
        return

    # Perform calculations
    sum_result = add(num1, num2)
    subtract_result = subtract(num1, num2)
    multiply_result = multiply(num1, num2)
    divide_result = divide(num1, num2)

    # Print and save results
    print_and_save_result("sum", num1, num2, sum_result)
    print_and_save_result("difference", num1, num2, subtract_result)
    print_and_save_result("product", num1, num2, multiply_result)
    print_and_save_result("quotient", num1, num2, divide_result)

if __name__ == "__main__":
    main()
