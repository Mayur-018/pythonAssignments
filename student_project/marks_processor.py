# marks_processor.py
import math

def calculate_average(marks_list):
    if not marks_list: return 0
    avg = sum(marks_list) / len(marks_list)
    return math.floor(avg) # Using math module

def get_grade(avg):
    if avg >= 90: return "A"
    elif avg >= 75: return "B"
    else: return "C"
