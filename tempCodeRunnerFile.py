import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

# Function to send email with an attachment
def send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, file_path):
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

        # Attach the file
        with open(file_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)  # Encode file in base64

            # Add header
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={file_path.split('/')[-1]}",
            )
            message.attach(part)

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)  # Login to your email account

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())
        print("Email with attachment sent successfully!")
    except Exception as e:
        print("Error sending email:", e)
    finally:
        server.quit()  # Close the connection

# Input details
sender_email = "en22cs304043@medicaps.ac.in"  # Your email
sender_password = "Pankaj@96"  # Your email password or app password
recipient_email = "pankajsaratkar33@gmail.com"  # Recipient's email
subject = "Personal Expense Managment System file"
body = "hy"
file_path = os.getcwd()

file_path = os.path.join(file_path,'nomarl.txt') # Full path to the file to attach

send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, file_path)
