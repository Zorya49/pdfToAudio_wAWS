import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_email = os.getenv('LOGIN')
smtp_password = os.getenv('PASSWORD')
smtp_server = "smtp-mail.outlook.com"
smtp_port = 587


class EmailSender:
    def __init__(self):
        self.from_email = smtp_email
        self.smtp_login = smtp_email
        self.smtp_password = smtp_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, subject, body, to_email):
        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        connection = smtplib.SMTP(self.smtp_server, port=self.smtp_port)
        connection.starttls()
        connection.login(user=self.smtp_login, password=self.smtp_password)
        connection.sendmail(from_addr=self.from_email,
                            to_addrs=to_email,
                            msg=msg.as_string())
        connection.quit()

