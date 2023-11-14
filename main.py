import glob
from pathlib import Path
from emailing import send_email

folders = [1,2,3,4,5]
for sales_files in folders:
    glob.glob("./[0-5].*.TXT", recursive=True)
    print(sales_files)


