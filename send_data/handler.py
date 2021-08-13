from send_data.decorators import time_logger
from datetime import datetime
from email.mime.text import MIMEText
import smtplib


@time_logger
def send_mail(timestamp, date, rates, preferred_currencies,
              sender_email, sender_email_password,
              reciever_name, reciever_email):

    now = datetime.now().strftime('%y %b %d, %A - %H:%M:%S')
    email_subject = f"Python Exchange Report for \
        {reciever_name} - ID: {timestamp} - Time: {now}"

    if preferred_currencies is not None:
        tmp = {exc: rates[exc] for exc in preferred_currencies}
        rates = tmp

    email_text = f"Hey {reciever_name},\n" + \
        f"This email shows the popular currencies sent automatically by python\n" + \
        f"BTC: {rates['BTC']},\tUSD: {rates['USD']},\tIRR: {rates['IRR']}\n" + \
        f"Thanks for following us.\n" + \
        f"MHGZ\n"

    send_smpt_email(email_subject, email_text, 
                    sender_email, sender_email_password, 
                    reciever_email)


def send_smpt_email(email_subject, email_text, 
                    sender_email, sender_email_password, 
                    reciever_email):
    
    # setup the mime
    msg = MIMEText(email_text)
    msg['Subject'] = email_subject
    msg['From'] = sender_email
    msg['To'] = reciever_email

    # creating
    with smtplib.SMTP('smtp.gmail.com', 587) as mail_server:
        print('\n\tSuccessfully connected to your gmail.')
        # enable security
        mail_server.starttls()
        mail_server.login(sender_email, sender_email_password)
        print('\tSuccessfully Logged In.')
        mail_server.sendmail(
            sender_email, reciever_email, msg.as_string())
        print('\tSuccessfully Your Message Sent.\n')
