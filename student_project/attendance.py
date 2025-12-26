# attendance.py
import datetime

# Dictionary to store student_id: [list of dates present]
attendance_records = {}


def mark_attendance(student_id):
    # Logs the current date for attendance
    today = datetime.date.today().strftime("%Y-%m-%d")
    if student_id not in attendance_records:
        attendance_records[student_id] = []

    if today not in attendance_records[student_id]:
        attendance_records[student_id].append(today)
        return f"Attendance marked for {student_id} on {today}."
    return f"Attendance already marked for {student_id} today."


def get_attendance_count(student_id):
    # Returns total days attended
    return len(attendance_records.get(student_id, []))
