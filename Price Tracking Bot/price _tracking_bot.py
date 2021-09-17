######################################
########                      ########
# https://github.com/halilumutyalcin #
########                      ########
######################################

import time

import requests
from bs4 import BeautifulSoup
import smtplib

url = ""
headers = {
    'User-Agent': ''}


def send_email(title):
    sender = ''
    receiver = ''
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender, '')
        subject = title + "price has gone down"
        body = url
        mail_content = f"To:{receiver}\nFrom:{sender}\nSubject:{subject}\n\n{body}"
        server.sendmail(sender, receiver, mail_content)
        print("its done.")
    except smtplib.SMTPException as e:
        print(e)
    finally:
        server.quit()


def check_price():
    page = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='product-name').get_text().strip()
    price = float(soup.find(id='offering-price').attrs.get('content'))
    print(title)
    print(price)
    want = 
    if price < want:
        send_email(title)
    else:
        pass


while True:
    check_price()
    time.sleep(60 * 60)
