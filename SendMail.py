#!/usr/bin/env python3
#@Kenji DURIEZ - [DeedWark] - 2020
#Send EMAIL

import smtplib
import socket
from datetime import date, datetime

RED = "\033[91m"
GREEN = "\033[92m"
END = "\033[00m"

def main():
    try:
        smtpsrv = input("SMTP Server: ")
        if not smtpsrv:
            print(RED+"SMTP Server required!"+END)
            exit()
        ehlo = input("EHLO: ")
        mfrom = input("MAIL FROM: ")
        rto = input("RCPT TO: ")
        if not rto:
            print(RED+"RCPT TO required!"+END)
            exit()
        cdate = input("Date (leave empty for current date or type 0 for none): ")
        if not cdate:
            cdate = date.today().strftime("%a %d %b %Y "+format(datetime.now(), '%H:%M:%S'))
        elif cdate == "0":
            pass
        tfrom = input("From: ")
        to = input("To: ")
        subject = input("Subject: ")
        mid = input("Message-Id (leave empty for random or type 0 for none): ")
        if not mid:
            b = date.today().strftime("%Y%m%d"+format(datetime.now(), '%H%M%S'))
            e = socket.gethostbyaddr(socket.gethostname())[0]
            mid = f"<{b}.9348@{e}>"
        elif mid == "0":
            pass
        xm = input("Mailer (leave empty for this one or type 0 for none): ")
        if not xm:
            xm = "PythonMailer"
        elif xm == "0":
            pass
        #CONTENT (MultiLine)
        multiline = []
        print("Content [Press 2x Enter to stop]: ")
        while True:
            contentline = input()
            if contentline:
                multiline.append(contentline)
            else:
                break
        contentall = '\n'.join(multiline)

        contentmore = f"""Date: {cdate}\nFrom: {tfrom}\nTo: {to}\nSubject: {subject}\nMessage-Id: {mid}\nX-Mailer: {xm}\n\n{contentall}"""
    except KeyboardInterrupt:
        print(RED+" Interrupted!")
        exit()


    try:
        smtpObj = smtplib.SMTP(smtpsrv, 25)
        smtpObj.sendmail(mfrom, rto, contentmore)
        print(GREEN+"250: Message sent")
        smtpObj.quit()
    except smtplib.SMTPException as e:
        print(RED+"Error - Message not sent!")
        print(e)
        exit()

if __name__ == '__main__':
    main()
