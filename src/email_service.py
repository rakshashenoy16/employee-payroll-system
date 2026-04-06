import smtplib
from email.message import EmailMessage
import os

def send_individual_email(sender_email, app_password, receiver_email, file_path, name):
    msg = EmailMessage()
    msg['Subject'] = f'Payslip for {name}'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    msg.set_content(f'Hello {name},\n\nPlease find your payslip attached.\n\nRegards,\nHR')

    with open(file_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(file_path)

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

    print(f" Sent to {receiver_email}")