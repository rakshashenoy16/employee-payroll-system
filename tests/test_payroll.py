import unittest
from src.processor import process_payroll

class TestPayroll(unittest.TestCase):

    def setUp(self):
        self.employees = [
            {
                "employee_id": "E001",
                "employee_name": "Test",
                "department": "IT",
                "monthly_salary": "30000"
            }
        ]

        self.attendance = [
            {"employee_id": "E001", "date": "2026-03-01", "status": "A"}
        ]

    def test_salary_deduction(self):
        _, payroll = process_payroll(
            self.employees,
            self.attendance,
            "config/config.json"
        )
        self.assertTrue(payroll[0]["deduction"] > 0)

    def test_final_salary(self):
        _, payroll = process_payroll(
            self.employees,
            self.attendance,
            "config/config.json"
        )
        self.assertTrue(payroll[0]["final_salary"] < 30000)

if __name__ == "__main__":
    unittest.main()