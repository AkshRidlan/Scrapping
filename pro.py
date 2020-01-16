import requests 
from bs4 import BeautifulSoup
import smtplib 
source="https://www.amazon.in/Test-Exclusive-746/dp/B07DJHXTLJ/ref=sr_1_1?keywords=oneplus+7&qid=1578824232&smid=A23AODI1X2CEAE&sr=8-1 "

head={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}


def Price_monitor():
    page=requests.get(source,headers=head)
    soup=BeautifulSoup(page.content,'html.parser')
    #print(soup.prettify())
    #Search for the product OnePlus
    product=soup.find(id="productTitle").get_text()

    cost=soup.find(id="priceblock_dealprice").get_text()

    converted_cost= cost[1:8]

    if(converted_cost < 30,000):
        Ack_mail()
    print(converted_cost)
    print(product.strip())

    if(converted_cost <30,000):
        Ack_mail()

def Ack_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('tp.swap@gmail.com','')

    subject ='Phone price fell down!'
    body='Check the link right now  https://www.amazon.in/Test-Exclusive-746/dp/B07DJHXTLJ/ref=sr_1_1?keywords=oneplus+7&qid=1578824232&smid=A23AODI1X2CEAE&sr=8-1 '
    msg= f"subject:{subject} \n\n {body}"

    server.sendmail(
        'tp.swap@gmail.com',
        'akshayridlan8@gmail.com',
        msg
    )
    print('Hey Mail has been sent!')

    server.quit()


Price_monitor()




