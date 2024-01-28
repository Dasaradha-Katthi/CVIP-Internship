import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from getpass import getpass

def read_recipients_csv(file_path):
    recipients = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            recipients.append(row)
    return recipients

def send_personalized_email(smtp_server, smtp_port, smtp_username, smtp_password, sender_email, subject, message_template, recipient):
    try:
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

       
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient['email']
        msg['Subject'] = subject

        personalized_message = message_template.format(**recipient)
        msg.attach(MIMEText(personalized_message, 'plain'))

       
        server.sendmail(sender_email, recipient['email'], msg.as_string())

        
        server.quit()

        print(f"Email sent successfully to {recipient['email']}")
    except Exception as e:
        print(f"Error sending email to {recipient['email']}: {str(e)}")

def main():
   
    SMTP_SERVER = input('Enter SMTP Server: ')
    SMTP_PORT = int(input('Enter SMTP Port: '))
    SMTP_USERNAME = input('Enter SMTP Username: ')
    SMTP_PASSWORD = getpass('Enter SMTP Password: ')
    SENDER_EMAIL = input('Enter Sender Email: ')

   
    SUBJECT = input('Enter Email Subject: ')
    MESSAGE_TEMPLATE = input('Enter Email Message Template (use {key} for placeholders): ')

   
    CSV_FILE_PATH = input('Enter CSV File Path (with recipient details): ')
    recipients = read_recipients_csv(CSV_FILE_PATH)

   
    for recipient in recipients:
        send_personalized_email(
            SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD,
            SENDER_EMAIL, SUBJECT, MESSAGE_TEMPLATE, recipient
        )

if __name__ == "__main__":
    main()
