import smtplib

import config


def send_email(subject, msg):
    try:
        reciever = ['zeshan.jamil@hotmail.com','mzjamil@lmkt.com','auburki@lmkr.com']
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS,reciever , message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = "Test subject"
msg = "Hello there, how are you today? This is a Mailing List test from python script. please ACK when recieved."

send_email(subject, msg)