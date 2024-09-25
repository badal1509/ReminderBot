import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time
from datetime import datetime

emailAddress = "badalsinghkushwaha023@gmail.com"  
emailPassword = "nnmk lctm rpbx gdyb" 
smtpServer = "smtp.gmail.com"
smtpPort = 465
#smtpPort = 587
#smtpPort = 25

def sendEmail(recipient, subject, message):
    try:
        
        msg = MIMEMultipart()
        msg['From'] = emailAddress
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))
        
        with smtplib.SMTP_SSL(smtpServer, smtpPort) as server:
            server.login(emailAddress, emailPassword)
            server.sendmail(emailAddress, recipient, msg.as_string())
            print(f"Email sent to {recipient} at {datetime.now()}")

    except Exception as e:
        print(f"Failed to send email: {e}")


def scheduleReminder(recipient, subject, message, reminderTime):
    print(f"Reminder scheduled for {reminderTime}")
    schedule.every().day.at(reminderTime).do(sendEmail, recipient, subject, message)


def main():
    recipient = "badal20010915@gmail.com"  
    subject = "Meeting Reminder"
    message = "This is a reminder for your meeting at 3 PM today."
    reminderTime = "18:39"  
    scheduleReminder(recipient, subject, message, reminderTime)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
