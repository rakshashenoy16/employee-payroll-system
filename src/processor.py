import json

def process_payroll(employees, attendance, config_path):
    with open(config_path) as f:
        config = json.load(f)

    working_days = config["working_days"]

    summary = {}
    payroll = []

    # Initialize employee
    for emp in employees:
        summary[emp['employee_id']] = {
            "name": emp['employee_name'],  # ✅ FIXED
            "present": 0,
            "absent": 0,
            "salary": float(emp['monthly_salary'])
        }

    # Count attendance
    for record in attendance:
        emp_id = record['employee_id']
        if emp_id not in summary:
            continue

        if record['status'] == "P":   # ✅ FIXED
            summary[emp_id]["present"] += 1
        elif record['status'] == "A": # ✅ FIXED
            summary[emp_id]["absent"] += 1

    # Payroll calculation
    for emp_id, data in summary.items():
        deduction = (data["salary"] / working_days) * data["absent"]
        final_salary = data["salary"] - deduction

        payroll.append({
            "employee_id": emp_id,
            "name": data["name"],
            "present_days": data["present"],
            "absent_days": data["absent"],
            "deduction": round(deduction, 2),
            "final_salary": round(final_salary, 2)
        })

    return summary, payroll