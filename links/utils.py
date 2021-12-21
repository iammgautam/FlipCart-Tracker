from bs4 import BeautifulSoup
import requests
import lxml

#function returns the title and price from the given url's .html file.
def get_link_data(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","DNT":"1", 
        "Connection":"close",
        "Upgrade-Insecure-Requests": "1",
        "Accepted-Language":"en-GB,en-US;q=0.9,en;q=0.8",
    }

    page = requests.get(url, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(class_ ='B_NuCI').get_text()
    title = title.strip()
    title = title.replace("\n            \n            "," ")

    price = soup2.find(class_='_30jeq3 _16Jk6d').get_text()
    price = price.strip()[1:]
    price1 = ''.join([str(int(x)) for x in price if x!=','])
    price1 = float(int(price1))
    # print(soup2)
    return title, price1
