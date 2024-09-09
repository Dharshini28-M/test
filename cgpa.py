def calculate_cgpa(subjects):
    total_credits = 0
    total_grade_points = 0

    for subject in subjects:
        grade, credits = subject
        total_credits += credits
        grade_points = {'S': 10, 'A': 9, 'B': 8, 'C': 7, 'D': 6, 'F': 0}
        total_grade_points += grade_points.get(grade.upper(), 0) * credits

    cgpa = total_grade_points / total_credits
    return cgpa

# Example usage:
subjects_list = [('A', 4), ('B', 3), ('S', 2)]  # List of (grade, credits) pairs
result_cgpa = calculate_cgpa(subjects_list)
print(f"Your CGPA is: {result_cgpa:.2f}")
