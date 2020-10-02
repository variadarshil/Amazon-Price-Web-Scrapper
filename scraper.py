import requests;
from bs4 import BeautifulSoup;
import smtplib

URL = 'https://www.amazon.in/Audio-Technica-ATH-M50x-Over-Ear-Professional-Headphones/dp/B00HVLUR86/ref=sr_1_15_sspa?crid=1INCSH7DJWBEQ&dchild=1&keywords=beats+headphones&qid=1600420722&s=electronics&sprefix=beats%2Celectronics%2C291&sr=1-15-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzM1kxTU8yRDdSMlpZJmVuY3J5cHRlZElkPUEwNDI1NTkzMzBOUExaTzlRWFpNUiZlbmNyeXB0ZWRBZElkPUEwNzk3NTE0MjBBSk42MUpENVhXUCZ3aWRnZXROYW1lPXNwX210ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=';

headers = {
    "User-Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}


def check_price():
    
    page = requests.get(URL, headers=headers);

    soup = BeautifulSoup(page.content, 'html.parser')

    # title = soup.find(id="productTitle")
    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = price[2:8]

    replace_unwanted_chars = int(converted_price.replace(',',''))
    print(replace_unwanted_chars)

    if(replace_unwanted_chars < 10000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo();
    server.starttls();
    server.ehlo();

    server.login('dvdev6634@gmail.com', "ADD YOUR KEY");

    subject = 'Price fell down'
    body = 'Check the amazon link https://www.amazon.in/Audio-Technica-ATH-M50x-Over-Ear-Professional-Headphones/dp/B00HVLUR86/ref=sr_1_15_sspa?crid=1INCSH7DJWBEQ&dchild=1&keywords=beats+headphones&qid=1600420722&s=electronics&sprefix=beats%2Celectronics%2C291&sr=1-15-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzM1kxTU8yRDdSMlpZJmVuY3J5cHRlZElkPUEwNDI1NTkzMzBOUExaTzlRWFpNUiZlbmNyeXB0ZWRBZElkPUEwNzk3NTE0MjBBSk42MUpENVhXUCZ3aWRnZXROYW1lPXNwX210ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('dvdev6634@gmail.com', 'variadarshil@gmail.com', msg)

    print('EMAIL SENT')

    server.quit()


    check_price()