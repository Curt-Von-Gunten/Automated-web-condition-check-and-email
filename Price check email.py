# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 10:54:23 2019

@author: Curt
"""

import requests #Alternative to urllib.
from bs4 import BeautifulSoup
import smtplib #For interacting with email server.
import time

URL = 'https://www.mtggoldfish.com/price/Mercadian+Masques/Cho-Mannos+Blessing#online'
headers = {'User-Agnent': 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers) #Headers specifies the browser of choice.
    soup = BeautifulSoup(page.content, 'html.parser')
    #soup.prettify() #For printing and/or inspecting.
    price = soup.find('div', {'class': 'price-box-price'}).get_text()
    price = float(price)
    
    if price < 2.00:
        send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()  
    server.login('SwellGadgets@gmail.com', 'ehfcsucwvthofgeb')
    
    subject = "Cho-Manno's Blessing is below $2.00!"
    body = "Here's the link: https://www.mtggoldfish.com/price/Mercadian+Masques/Cho-Mannos+Blessing#online"
    msg = f"Subject: {subject}\n\n{body}"
    #msg = 'Subject: {}\n\n{}'.format(subject, body) #alternative appraoch without f.
    server.sendmail('SwellGadgets@gmail.com', 'SwellGadgets@gmail.com', msg)
    print("The email was sent")
    server.quit()

#check_price
while True:
    check_price()
    time.sleep(60*60*48) #Check the price every two days.