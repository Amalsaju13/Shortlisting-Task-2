Serverless Email Sender API (Python + AWS Lambda)

A simple REST API built with the Serverless Framework and Python that sends emails using Gmail SMTP.  
Supports local development using `serverless-offline` and can be deployed to AWS Lambda easily.

---

 Features

- ✅ REST API with `POST /send-email`
- ✅ Email sending via Gmail SMTP
- ✅ Uses environment variables via `.env`
- ✅ Error handling with proper HTTP responses
- ✅ Local testing with `serverless-offline`
- ✅ Deployable to AWS Lambda + API Gateway

---
 Request Format

**Endpoint (Local):**
POST http://localhost:3000/dev/send-email



**Request Body (JSON):**
```json
{
  "receiver_email": "example@example.com",
  "subject": "Hello from Apputtan",
  "body_text": "This is a test email sent from the Serverless Python API."
}

 Setup & Run Locally

1. Clone the repo
git clone https://github.com/your-username/serverless-email-api.git
cd serverless-email-api

2. Install dependencies

npm install
pip install python-dotenv

3. Create .env file
env

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_gmail_app_password

Use a Gmail App Password (not your real password).
Enable 2FA and generate it at: https://myaccount.google.com/apppasswords

4. Run locally
npx serverless offline

Project Structure
bash
Copy
Edit
serverless-email-api/
├── handler.py         # Main Lambda function
├── serverless.yml     # Serverless Framework config
├── package.json       # Dev dependencies (serverless-offline)
├── .env               # Gmail credentials (excluded in Git)
├── .gitignore         # Ignored files/folders
└── README.md          # This file

✅ Sample Response
Success (200):

json

{
  "message": "Email sent successfully"
}
Error (400 or 500):

json
{
  "error": "Missing required fields"
}
