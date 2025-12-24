# Case Study 1: Student Grade Calculator

def calculate_grade(average):
    # Assigns a letter grade based on the average marks
    if average >= 90:
        return "A"
    elif 75 <= average <= 89:
        return "B"
    elif 60 <= average <= 74:
        return "C"
    else:
        return "Fail"


# Initialize an empty dictionary
students_data = {}

# 1. Take input for 5 students
print("Enter details for 5 students:")
for i in range(5):
    name = input(f"\nEnter name for student {i + 1}: ")
    marks = []

    # Collect marks for 3 subjects
    for j in range(3):
        while True:
            try:
                m = float(input(f"  Enter marks for Subject {j + 1}: "))
                marks.append(m)
                break
            except ValueError:
                print("  Invalid input! Please enter a numeric value.")

    # Store in dictionary
    students_data[name] = marks


def process_student_results(data):
    top_scorer = ""
    highest_avg = -1  # Initialize lower than possible marks

    print("\n" + "=" * 35)
    print(f"{'Name':<10} | {'Average':<10} | {'Grade'}")
    print("-" * 35)

    for name, marks in data.items():
        # 2. Calculate average marks
        avg_marks = sum(marks) / len(marks)

        # 3. Assign grades
        grade = calculate_grade(avg_marks)

        # 4. Print student name, average, and grade
        print(f"{name:<10} | {avg_marks:<10.2f} | {grade}")

        # 5. Track the top scorer
        if avg_marks > highest_avg:
            highest_avg = avg_marks
            top_scorer = name

    print("-" * 35)
    print(f"Top Scorer: {top_scorer} with an average score of {highest_avg:.2f}")


# Execute the processing function
process_student_results(students_data)
