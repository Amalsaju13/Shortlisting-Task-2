import os
import json
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def send_email(event, context):
    try:
        data = json.loads(event.get("body", "{}"))

        receiver_email = data.get("receiver_email")
        subject = data.get("subject")
        body_text = data.get("body_text")

        if not receiver_email or not subject or not body_text:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing required fields"})
            }

        smtp_server = os.getenv("SMTP_SERVER")
        smtp_port = int(os.getenv("SMTP_PORT", 587))
        sender_email = os.getenv("SENDER_EMAIL")
        sender_password = os.getenv("SENDER_PASSWORD")

        message = MIMEText(body_text)
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = receiver_email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Email sent successfully"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
