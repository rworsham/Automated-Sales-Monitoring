import smtplib, ssl
from email.message import EmailMessage
import time
import os



polled_sales = []

class Send:
    def email(self, message):

        msg = EmailMessage()
        msg.set_content(message)

        msg['Subject'] = 'Test Sales'
        msg['From'] = "dalcomsalesmonitor@gmail.com"
        msg['To'] = "rworsham@dalcom.com"

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("dalcomsalesmonitor@gmail.com", "uclt cmdg ksuw wego")
        server.send_message(msg)
        server.quit()

class Check:
    def path(self):
        subfolders = [sub.path for sub in os.scandir("./") if sub.is_dir()]
        for count in subfolders:

            return subfolders

    def grab(self, filepath):
        self.filepath = filepath
        if os.path.exists(filepath):
            polled_sales.append(f"{filepath} has polled!")
        else:
            pass


check = Check()
check.grab("1/STORESALES01.TXT")
check.grab("2/STORESALES02.TXT")
check.grab("3/STORESALES03.TXT")
check.grab("4/STORESALES04.TXT")
check.grab("5/STORESALES05.TXT")



while True:
    current_time = time.strftime("%H:%M")
    if current_time == "13:57":
        send = Send()
        print(polled_sales)
        print(check.path())
        string_convert = str(polled_sales)
        message = f"""
        Below is the list of Stores that have polled, compare the list below to the spreadsheet and proceed accordingly. \n
        {polled_sales}
        """
        print("process completed")
        send.email(message)
        time.sleep(60)




