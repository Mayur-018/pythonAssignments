# reports.py
import datetime

class StudentReport:
    def __init__(self, name, average, grade):
        self.name = name
        self.average = average
        self.grade = grade
        self.date = datetime.date.today() # Using datetime module

    def display_report(self):
        print(f"\n--- Progress Report ---")
        print(f"Date: {self.date}")
        print(f"Student: {self.name}")
        print(f"Average: {self.average}")
        print(f"Grade: {self.grade}")
