# finance.py

# Dictionary to store student_id: balance
fee_balances = {}
TUITION_FEE = 50000.00

def initialize_fees(student_id):
    # Sets initial balance for new entry
    fee_balances[student_id] = TUITION_FEE

def pay_fees(student_id, amount):
    # Deducts payment
    if student_id in fee_balances:
        fee_balances[student_id] -= amount
        return f"Payment of INR {amount} received. Remaining: INR {fee_balances[student_id]}"
    return "Student record not found in finance system."

def get_status(student_id):
    # Checks if fees are fully paid
    balance = fee_balances.get(student_id, 0)
    if balance <= 0:
        return "Paid"
    return f"Pending: INR {balance}"
