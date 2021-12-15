from bs4 import BeautifulSoup
import requests

url = 'https://www.amazon.in/Xbox-Series-S/dp/B08J89D6BW/ref=sr_1_4?crid=W4UH15RLIDXB&keywords=xbox+series+x&qid=1639579345&sprefix=xbox%2Caps%2C456&sr=8-4'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","DNT":"1", 
    "Connection":"close", 
    "Upgrade-Insecure-Requests": "1",
    "Accepted-Language":"en",
    }

page = requests.get(url, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id ='productTitle').get_text()
title = title.strip()

price = soup2.find(id='priceblock_ourprice').get_text()    
price = price.strip()[1:]

def get_link_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","DNT":"1", 
        "Connection":"close", 
        "Upgrade-Insecure-Requests": "1",
        "Accepted-Language":"en",
    }

    page = requests.get(url, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id ='productTitle').get_text()
    title = title.strip()

    price = soup2.find(id='priceblock_ourprice').get_text()    
    price = price.strip()[1:]

    return title, price



    
print(get_link_data(url))