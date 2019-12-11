import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Apple-MacBook-13-inch-1-8GHz-Dual-core/dp/B073Q5R6VR?tag=googinhydr18418-21&tag=googinkenshoo-21&ascsubtag=_k_CjwKCAjw1f_pBRAEEiwApp0JKIrQZ1qcvacwVsuTrnbMIdZWdrmyq4b8qLjNvJmKarbLPylGbRU5YBoCHLsQAvD_BwE_k_&gclid=CjwKCAjw1f_pBRAEEiwApp0JKIrQZ1qcvacwVsuTrnbMIdZWdrmyq4b8qLjNvJmKarbLPylGbRU5YBoCHLsQAvD_BwE'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}



    
def check_price():
    
    page = requests.get(URL,headers = headers)
    soup = BeautifulSoup(page.content,'html.parser')
     #print(soup.prettify())    
    title = soup.find(id = "productTitle").get_text()    
    price = soup.find(id = "priceblock_ourprice").get_text()
    price = (price.translate({ord(','): None}))
    converted_price = float(price[2:7])
    if(converted_price < 50000):
        send_mail()
    print(title.strip())
    print(converted_price)
    
def send_mail():
    
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('YOUR_EMAIL','your_gmail_authentication_password')
    #kind of temporary password to access your gmail mailing service
    
    subject = 'MakerSpace Project'
    body = 'check this thing quickly https://www.amazon.in/Apple-MacBook-13-inch-1-8GHz-Dual-core/dp/B073Q5R6VR?tag=googinhydr18418-21&tag=googinkenshoo-21&ascsubtag=_k_CjwKCAjw1f_pBRAEEiwApp0JKIrQZ1qcvacwVsuTrnbMIdZWdrmyq4b8qLjNvJmKarbLPylGbRU5YBoCHLsQAvD_BwE_k_&gclid=CjwKCAjw1f_pBRAEEiwApp0JKIrQZ1qcvacwVsuTrnbMIdZWdrmyq4b8qLjNvJmKarbLPylGbRU5YBoCHLsQAvD_BwE'
    msg = f"Subject: {subject}\n\n\n{body}"
    
    server.sendmail('SENDERS_EMAIL','RECEIVERS_EMAIL',msg)
    #SENDERS_ADDRESS could be different from your email address
    print('hey email has been sent')
    server.quit()

    
while(True):
    check_price()
    time.sleep(60*60*60)





