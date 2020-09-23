import smtplib
import socket

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

s=socket.socket()
port = 453
s.connect((smtp.gmail.com,587))
s.listen()
print(s.recv(587))

sender = rrromeo101@gmail.com
receivers = [zeshan.jamil@hotmail.com]

message = """this is a test email"""

try:
	smtpObj = smtplib.SMTP("smtp.gmail.com",587)
	smtpObj.sendmail(sender,receivers,message)
	print("success")

except Exception:
	print("fail")
s.close()