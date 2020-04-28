from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import smtplib
from datetime import date
import shutil

cwd = os.getcwd()
x = str(date.today()).replace("-", "")


def setEmail(sender, password, reciever):
    global fromaddr, toaddr, passkey
    fromaddr = sender
    toaddr = reciever
    passkey = password


def sendEmail(image, num, img1):
    # fromaddr = "persondetection1@gmail.com"
    # change the Email Address of receiver
    # toaddr = "alaspure.amh@gmail.com"
    # passkey = "person@123"

    # instance of MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "[NNTO] Test mail Python with attachment"
    body = str(num) + " person detected"

    msg.attach(MIMEText(body, 'plain'))
    for i in image:
        # open the file to be sent
        filename = os.path.basename(i)
        attachment = open(i, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
    filename = os.path.basename(img1)
    attachment = open(filename, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, passkey)
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()


if __name__ == '__main__':
    # imageList = ['8383_faces.jpg', '6666_faces.jpg', '6969_faces.jpg', '8484_faces.jpg']
    # count = len(imageList)
    # newImage  = 'faces_detected.jpg'
    # sendEmail(imageList, count, newImage)
    print("through main")
