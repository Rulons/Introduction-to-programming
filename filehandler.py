def read_data(input_filename):
    # This function reads data from a file and stores it in a dictionary
    students_data = {}

    with open(input_filename, 'r') as file:
        for line in file:
            # Skip empty lines
            if line.strip() == '':
                continue
            
            # Process each line (assuming format: name, unit, mark, weight)
            parts = line.strip().split(',')
            if len(parts) == 4:  # Ensure there are 4 elements in the line
                name, unit, mark, weight = parts
                mark = float(mark)
                weight = float(weight)
                
                # Check if the student is already in the dictionary
                if name not in students_data:
                    students_data[name] = []
                
                # Append the (unit, mark, weight) tuple for the student
                students_data[name].append((unit, mark, weight))

    return students_data

def calculate_weighted_grade(student_data):
    # This function calculates the weighted grade for a student
    total_weight = 0
    weighted_sum = 0
    for unit, mark, weight in student_data:
        weighted_sum += mark * (weight / 100)
        total_weight += weight
    
    if total_weight != 100:
        raise ValueError(f"Total weight for {student_data[0][0]} does not add up to 100!")
    
    return weighted_sum

def determine_grade(weighted_grade):
    # This function determines the grade based on the weighted grade
    if weighted_grade >= 85:
        return "Distinction"
    elif weighted_grade >= 65:
        return "Merit"
    elif weighted_grade >= 50:
        return "Pass"
    else:
        return "Fail"

def write_results_to_file(output_filename, student_results):
    # This function writes the final results to an output file
    with open(output_filename, 'w') as file:
        for name, weighted_grade, grade in student_results:
            file.write(f"{name}, {weighted_grade:.2f}, {grade}\n")

def main():
    input_filename = 'students_input.txt'
    output_filename = 'students_results.txt'
    
    # Read data from the input file
    students_data = read_data(input_filename)
    
    results = []
    # Loop over each student and calculate their weighted grade and final grade
    for name, data in students_data.items():
        weighted_grade = calculate_weighted_grade(data)
        grade = determine_grade(weighted_grade)
        results.append((name, weighted_grade, grade))
    
    # Write the results to the output file
    write_results_to_file(output_filename, results)

# Run the main function
if __name__ == "__main__":
    main()
