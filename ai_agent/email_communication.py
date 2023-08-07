```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from environment_setup import communication_details

def send_email(subject, message):
    msg = MIMEMultipart()
    msg['From'] = communication_details['email_address']
    msg['To'] = 'recipient@example.com'
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(communication_details['email_address'], communication_details['email_password'])
    text = msg.as_string()
    server.sendmail(communication_details['email_address'], 'recipient@example.com', text)
    server.quit()
```