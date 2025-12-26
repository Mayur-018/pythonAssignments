# data_manager.py
students = {}

def add_student(student_id, name):
    students[student_id] = {"name": name}
    print(f"Student {name} added successfully.")

def get_student(student_id):
    return students.get(student_id, "Student not found.")

# Demonstrating built-in properties
if __name__ == "__main__":
    print(f"Module Name: {__name__}")
    print(f"File Path: {__file__}")
