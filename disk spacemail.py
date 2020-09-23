import subprocess
import smtplib
from email.mime.text import MIMEText
threshold = 20
partition = “/”
def report_via_email():
 msg = MIMEText(“Server running out of disk space”)
 msg[“Subject”] = “Low disk space warning”
 msg[“From”] = “rrromeo101@gmail.com”
 msg[“To”] = “zexjimmy@hotmail.com”
 with smtplib.SMTP(“smtp.gmail.com”, 587) as server:
 server.ehlo()
 server.starttls()
 server.login(“rrromeo101@gmail.com”,”sisskixx101)
 server.sendmail(“zexjimmy@hotmail.com”,”zeshan.jamil@hotmail.com”,msg.as_string())
def check_once():
 df = subprocess.Popen([“df”,”-h”], stdout=subprocess.PIPE)
 for line in df.stdout:
 splitline = line.decode().split()
 if splitline[5] == partition:
 if int(splitline[4][:-1]) > threshold:
 report_via_email()
check_once()