from src.loader import load_csv
from src.validator import validate_records
from src.processor import process_payroll
from src.report import write_csv
from src.logger import log_error

employees = load_csv("data/employees.csv")
attendance = load_csv("data/attendance.csv")

valid_attendance, errors = validate_records(employees, attendance)

log_error(errors, "output/error_log.csv")

summary, payroll = process_payroll(
    employees,
    valid_attendance,
    "config/config.json"
)

write_csv(payroll, "output/payroll_report.csv")

summary_list = [
    {
        "employee_id": k,
        **v
    } for k, v in summary.items()
]

write_csv(summary_list, "output/attendance_summary.csv")

print("Processing Complete!")