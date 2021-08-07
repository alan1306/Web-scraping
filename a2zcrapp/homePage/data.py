from requests_html import HTMLSession
from bs4 import BeautifulSoup
class Product():
    def __init__(self,name,price,rating):
        self.name=name
        self.price=price
        self.rating=rating
    def __repr__(self):
        return self.name

s=HTMLSession()

url="https://www.amazon.in/s?bbn=976419031&rh=n%3A976419031%2Cp_89%3Arealme&dc"


def getData(url):
    r=s.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    return soup

def findE(soup):
    productList=[]
    page=soup.find('div',{'class':'s-main-slot s-result-list s-search-results sg-row'},'html.parser')
    next=page.find_all('div',{'class':'sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20'})
    for items in next:
        productName=items.find('span',{'class':'a-size-base-plus a-color-base a-text-normal'}).text
        productPrice=int(items.find('span',{'a-price-whole'}).text.replace(',',''))
        productRating=float(items.find('span',{'a-icon-alt'}).text.split()[0])
        p=Product(productName,productPrice,productRating)
        productList.append(p)
    return productList