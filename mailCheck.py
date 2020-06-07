from xsmtplib import SMTP

login = "thusynov2020@mail.ru"
password = ""


def check(log, passw):
    server = SMTP(host="smtp.mail.ru")
    server.starttls()

    try:
        server.login(log, passw)
    except:
        print("Not Found!")
        server.quit()
        return
    print("Found: " + passw)
    server.quit()


check(login, password)
