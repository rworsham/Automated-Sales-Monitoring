import glob
from pathlib import Path
from emailing import send_email



sales_files = glob.glob("./[1-5]/*.TXT")
polled_sales = str(sales_files)
send_email(polled_sales)
print(polled_sales)


