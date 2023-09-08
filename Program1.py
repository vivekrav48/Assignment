def calculate_final_grade(subject1, subject2, subject3, subject4):
    total_marks = subject1 + subject2 + subject3 + subject4
    average_marks = total_marks / 4

    if average_marks >= 60:
        return "A", "Pass"
    elif average_marks >= 50:
        return "B", "Pass"
    elif average_marks >= 40:
        return "C", "Pass"
    else:
        return "F", "Fail"

# Input marks
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
subject4 = float(input("Enter marks for subject 4: "))

# Calculate final grade
grade, status = calculate_final_grade(subject1, subject2, subject3, subject4)

# Print the results
print(f"Final Grade: {grade}")
print(f"Status: {status}")
