#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import datetime
import smtplib
import sys

from email import Encoders
from email.Utils import formatdate
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def create_message(from_addr, to_addr, subject, body, attach_file):
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Date"] = formatdate()

    body = MIMEText(body)
    msg.attach(body)

    if attach_file != '':
        attachment = MIMEBase("application","octet-stream")
        file = open(attach_file)
        attachment.set_payload(file.read())
        file.close()
        Encoders.encode_base64(attachment)
        msg.attach(attachment)
        attachment.add_header("Content-Disposition","attachment", filename=attach_file)

    return msg

def send(from_addr, to_addrs, msg):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('<user>', '<pass>')
    smtp.sendmail(from_addr, to_addrs, msg.as_string())
    smtp.close()

if __name__ == '__main__':

    if len(sys.argv) < 4:
        print 'usage : python %s script' % sys.argv[0]
        quit()

    from_addr = '<user>@gmail.com'
    to_addr = sys.argv[1]
    subject = sys.argv[2]
    body = sys.argv[3]
    attach = ''
    if len(sys.argv) > 4:
        attach = sys.argv[4]

    msg = create_message(from_addr, to_addr, subject, body, attach)
    send(from_addr, to_addr, msg)
