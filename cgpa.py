def calculate_cgpa_with_user_input():
    total_credits = 0
    total_grade_points = 0

    # Mapping of letter grades to grade points
    grade_points = {'S': 10, 'A': 9, 'B': 8, 'C': 7, 'D': 6, 'F': 0}

    num_subjects = int(input("Enter the number of subjects: "))

    for _ in range(num_subjects):
        grade = input("Enter the grade (S/A/B/C/D/F): ").upper()
        credits = float(input("Enter the credits for this subject: "))
        
        total_credits += credits
        total_grade_points += grade_points.get(grade, 0) * credits

    cgpa = total_grade_points / total_credits
    return cgpa

# Example usage:
result_cgpa = calculate_cgpa_with_user_input()
print(f"Your CGPA is: {result_cgpa:.2f}")
