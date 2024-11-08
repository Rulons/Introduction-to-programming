# functions.py

def convert_temperature(temp, conversion_type):
    """Converts temperature based on conversion_type."""
    if conversion_type == 'C to F':  # Celsius to Fahrenheit
        return (temp * 9/5) + 32
    elif conversion_type == 'F to C':  # Fahrenheit to Celsius
        return (temp - 32) * 5/9
    else:
        return "Invalid conversion type"

def main():
    """Main function to get user input and display result."""
    # Get user input for conversion type
    print("Temperature Conversion Options:")
    print("1. Celsius to Fahrenheit (C to F)")
    print("2. Fahrenheit to Celsius (F to C)")
    conversion_type = input("Enter conversion type (C to F or F to C): ")

    # Get user input for temperature value
    try:
        temp = float(input("Enter the temperature value: "))
    except ValueError:
        print("Please enter a valid number for temperature.")
        return

    # Perform the conversion
    converted_temp = convert_temperature(temp, conversion_type)

    # Display the result
    if isinstance(converted_temp, str):
        print(converted_temp)  # If there was an invalid conversion type
    else:
        print(f"The converted temperature is: {converted_temp:.2f}")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
