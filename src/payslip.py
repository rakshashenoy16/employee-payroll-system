import csv
import os

def generate_payslips(payroll_data):
    os.makedirs("output/payslips", exist_ok=True)

    file_paths = {}

    for emp in payroll_data:
        file_name = f"output/payslips/{emp['employee_id']}_payslip.csv"

        with open(file_name, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=emp.keys())
            writer.writeheader()
            writer.writerow(emp)

        file_paths[emp['employee_id']] = file_name

    return file_paths