import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import os


# Function to send email with an attachment
def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # SMTP server and port
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Create the email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject

        # Add the email body
        message.attach(MIMEText(body, "plain"))

    

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)  # Login to your email account

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())
        return True
        
    except Exception as e:
        return False

    finally:
        server.quit()  # Close the connection



