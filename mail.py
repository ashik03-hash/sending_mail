# how to send real time mail using python simple mail transfer protocol library(smiplib)
# starttls(start transport layer security)

import smtplib
import random

f=open("stu_mail.txt","r")
student_mail=f.read()


student_mail=student_mail.split(",")
print(student_mail)

sender_mail="mashikashi03@gmail.com"

for i in student_mail:
    otp_num=random.randint(0000,9999)
    s=smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login(sender_mail,"*************")
    message=f"Hi! your OTP is{otp_num}" 
    print(message)
    s.sendmail(sender_mail,i,message)
    s.quit()