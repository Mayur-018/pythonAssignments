# main.py
import data_manager
import marks_processor as mp      # Module Alias
from attendance import mark_attendance, get_attendance_count # Specific imports
import finance as fin             # Module Alias
import reports                    # Standard import
import random                     # Predefined module


def display_menu():
    print("\n---  Student Management System 2025 ---")
    print("1. Register New Student")
    print("2. Mark Attendance")
    print("3. Process Marks & Generate Report")
    print("4. Fee Payment")
    print("5. View Module Metadata")
    print("6. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            sid = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            data_manager.add_student(sid, name)
            fin.initialize_fees(sid)
            print(f"Success: {name} registered with Temp Passcode: {random.randint(1000, 9999)}")

        elif choice == '2':
            sid = int(input("Enter Student ID to mark attendance: "))
            # Verify student exists
            student = data_manager.get_student(sid)
            if isinstance(student, dict):
                result = mark_attendance(sid)
                print(result)
            else:
                print(f"Error: {student}")  # Prints "Student not found"

        elif choice == '3':
            sid = int(input("Enter Student ID for report: "))
            # Verify student exists
            student = data_manager.get_student(sid)
            if isinstance(student, dict):
                marks_input = input("Enter marks separated by space: ")
                marks_list = [float(m) for m in marks_input.split()]

                avg = mp.calculate_average(marks_list)
                grade = mp.get_grade(avg)

                report = reports.StudentReport(student['name'], avg, grade)
                report.display_report()
                print(f"Total Days Attended: {get_attendance_count(sid)}")
            else:
                print(f"Error: {student}")

        elif choice == '4':
            sid = int(input("Enter Student ID for payment: "))
            # Verify student exists 
            student = data_manager.get_student(sid)
            if isinstance(student, dict):
                print(f"Student Found: {student['name']}")
                print(f"Current Status: {fin.get_status(sid)}")
                amount = float(input("Enter payment amount: "))
                print(fin.pay_fees(sid, amount))
            else:
                print(f"Error: {student}")

        elif choice == '5':
            print(f"\n--- Module Metadata ---")
            print(f"Data Manager Name: {data_manager.__name__}")
            print(f"Data Manager File: {data_manager.__file__}")
            print(f"Marks Processor Dictionary: {list(mp.__dict__.keys())[:5]}...")

        elif choice == '6':
            print("Exiting System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
