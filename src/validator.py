from datetime import datetime

def validate_records(employees, attendance):
    valid = []
    errors = []

    emp_ids = {e['employee_id'] for e in employees}

    for record in attendance:
        # Checks if employee exists
        if record['employee_id'] not in emp_ids:
            errors.append({"error": "Invalid Employee", "record": str(record)})
            continue

        # Check valid date
        try:
            datetime.strptime(record['date'], "%Y-%m-%d")
        except:
            errors.append({"error": "Invalid Date", "record": str(record)})
            continue

        valid.append(record)

    return valid, errors