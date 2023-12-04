import smtplib
from email.message import EmailMessage
import time
import os

#Created and tested by R. Worsham

polled_sales = []


class Send:
    def email(self, message):

        msg = EmailMessage()
        msg.set_content(message)

        msg['Subject'] = 'Triad Sales'
        msg['From'] = "Dalcom Sales Monitor"
        msg['To'] = "rworsham@dalcom.com"

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("dalcomsalesmonitor@gmail.com", "uclt cmdg ksuw wego")
        server.send_message(msg)
        server.quit()


class Check:
    def grab(self, filepath):
        self.filepath = filepath
        if os.path.exists(filepath):
            if filepath not in polled_sales:
                polled_sales.append(filepath)
                print(polled_sales)
            else:
                pass


while True:
    current_time = time.strftime("%H:%M")
    check = Check()
    check.grab("C:\\INV\\IN\\1\\STORE001.TXT")
    check.grab("C:\\INV\\IN\\2\\STORE002.TXT")
    check.grab("C:\\INV\\IN\\3\\STORE003.TXT")
    check.grab("C:\\INV\\IN\\4\\STORE004.TXT")
    check.grab("C:\\INV\\IN\\5\\STORE005.TXT")
    check.grab("C:\\INV\\IN\\6\\STORE006.TXT")
    check.grab("C:\\INV\\IN\\7\\STORE007.TXT")
    check.grab("C:\\INV\\IN\\8\\STORE008.TXT")
    check.grab("C:\\INV\\IN\\9\\STORE009.TXT")
    check.grab("C:\\INV\\IN\\10\\STORE010.TXT")
    check.grab("C:\\INV\\IN\\12\\STORE012.TXT")
    check.grab("C:\\INV\\IN\\14\\STORE014.TXT")
    check.grab("C:\\INV\\IN\\15\\STORE015.TXT")
    check.grab("C:\\INV\\IN\\16\\STORE016.TXT")

    print("Polling Folders Checked")
    time.sleep(5)
    if current_time == "22:15" or len(polled_sales) == 14:
        send = Send()
        polled_sales_data = ("\n".join(polled_sales))
        number_of_sales = len(polled_sales)
        message = f"""
        Below is the list of Stores that have polled, compare the list below to the spreadsheet and proceed accordingly. 
        
        Results Returned: {number_of_sales}                 Expected: 14

{polled_sales_data}
        
        """
        print("Sending Email now, Goodnight!")
        send.email(message)
        time.sleep(60)
        exit()
