#  Employee Attendance & Payroll Processing System

##  Overview

This project is a Python-based Payroll Processing System that automates employee attendance tracking, salary calculation, and payroll report generation.

It simulates real-world HR workflows by:

* Validating attendance data
* Calculating salary deductions
* Generating reports
* Creating individual payslips
* Sending payslips via email

---

##  Features

###  Core Features

* Load employee & attendance data from CSV files
* Validate:

  * Employee existence
  * Date format
* Calculate:

  * Present days
  * Absent days
  * Salary deductions
* Generate:

  * Payroll report
  * Attendance summary


### Advanced Features (WOW Factor)

* Individual payslip generation (per employee)
*  Automated email delivery of payslips
* Error logging for invalid records
* Config-driven payroll rules
*  Unit testing using `unittest`
* Git feature-branch workflow

---

## Project Structure

```
employee_payroll_system/
│
├── data/
│   ├── employees.csv
│   ├── attendance.csv
│
├── output/
│   ├── payroll_report.csv
│   ├── attendance_summary.csv
│   ├── error_log.csv
│   ├── payslips/
│
├── config/
│   └── config.json
│
├── src/
│   ├── loader.py
│   ├── validator.py
│   ├── processor.py
│   ├── report.py
│   ├── logger.py
│   ├── payslip.py
│   ├── email_service.py
│
├── tests/
│   └── test_payroll.py
│
├── main.py
├── requirements.txt
└── README.md
```


##  Setup Instructions

###  Clone Repository

```
git clone <your-repo-url>
cd employee_payroll_system
```



##  How to Run

```
python main.py
```

---

##  Output Files

Generated in `output/` folder:

* `payroll_report.csv` → Salary details
* `attendance_summary.csv` → Attendance breakdown
* `error_log.csv` → Invalid records
* `payslips/` → Individual employee payslips

---
## Email Functionality

The system can send **individual payslips via email**.

###  Setup Gmail App Password

1. Enable **2-Step Verification** in your Google account
2. Go to **App Passwords**
3. Generate password for Mail
4. Use it in code

---

###  Configure in `main.py`

```
SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"
```

---

### Important

* Do NOT use your real email password
* Use App Password only
* Do NOT push credentials to GitHub



##  Run Tests

```
python -m unittest discover tests
```

---

## Git Workflow

### Create Feature Branch

```
git checkout -b feature/enhancements
```

### Commit Changes

```
git add .
git commit -m "Added new feature"
```

### Push Branch

```
git push origin feature/enhancements
```



##  .gitignore Notes

* Output files are excluded
* Sensitive data should not be committed



##  Key Learnings

* Modular Python architecture
* Data validation and error handling
* File processing using CSV
* SMTP-based email automation
* Unit testing practices
* Git branching strategies

---

##  Future Enhancements

*  PDF payslip generation
*  Web UI using Flask
*  Dashboard with charts
*  Database integration
*  Role-based access




