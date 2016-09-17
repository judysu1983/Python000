import smtplib, socket, sys, getpass
smtpserver=smtplib.SMTP("smtp.gmail.com",25)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
print("yes")
