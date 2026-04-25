import smtplib
from email.message import EmailMessage

def send_email(receiver):
    msg = EmailMessage()
    msg['Subject'] = 'Automated Report'
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = receiver

    with open("reports/report.pdf", "rb") as f:
        msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename='report.pdf')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('your_email@gmail.com', 'app_password')
        smtp.send_message(msg)