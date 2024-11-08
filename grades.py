mark = float(input("Enter the sudents's mark:"))

if mark >= 70:
    grade = "A"
elif 60 <= mark < 70:
    grade = "B"
elif 50 <= mark < 60:
    grade = "C"
elif 40 <= mark <50:
    grade = "D"
elif 30 <= mark <40:
    grade = "E"
elif 20 <= mark < 30:
    grade = "F"
else:
    grade = "Invalid mark. Please enter a mark between 20 and 100."

# Printing the grade
print(f"The student's grade is: {grade}")

    
