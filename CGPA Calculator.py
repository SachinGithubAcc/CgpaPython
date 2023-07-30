def calculate_grade_point(grade):
    if grade == 'O':
        return 10.0

    elif grade == 'A+':
        return 9.0

    elif grade == 'A':
        return 8.0

    elif grade == 'B+':
        return 7.0

    elif grade == 'B':
        return 6.0

    elif grade == 'C':
        return 5.0

    elif grade == 'D':
        return 4.0

    elif grade == 'F':
        return 0.0-39.99
    else:
        return None

def main():
    num_subjects = int(input("Enter the number of subjects: "))
    total_credit_hours = 0
    total_weighted_grade_points = 0

    for i in range(num_subjects):
        grade = input(f"Enter the grade for subject {i+1}: ").upper()
        credit_hours = float(input(f"Enter the credit hours for subject {i+1}: "))

        grade_point = calculate_grade_point(grade)
        if grade_point is None:
            print("Invalid grade entered. Please try again.")
            return

        weighted_grade_point = grade_point * credit_hours
        total_credit_hours += credit_hours
        total_weighted_grade_points += weighted_grade_point

    cgpa = total_weighted_grade_points / total_credit_hours

    print(f"\nYour CGPA is: {cgpa:.2f}")
if __name__ == "__main__":
    main()

