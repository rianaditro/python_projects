from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re

def access(url):
    session = HTMLSession()
    r = session.get(url)
    r.html.render(sleep=1)
    return r

def get_all_links(main_url):
    r = access(main_url)
    product_links = r.html.xpath('//*[@id="product-list-component"]/div[4]/div', first=True).absolute_links
    return product_links

def parse_product(product_url):
    r = access(product_url)
    soup = BeautifulSoup(r.html.html,"html.parser")
    name = find_data("div","d-flex flex-row",soup)
    summary = find_data("span", "itemFacts font-weight-normal",soup)
    price = find_data("p","itemNormalPrice display-6",soup)
    price = re.findall(r'[\d]+',price)

    result = {"product name":name,
              "url":product_url}
    return result

def find_data(tag, class_,soup):
    data = soup.find(tag,class_).get_text().strip
    return data

if __name__=="__main__":
    main_url = "https://www.ikea.co.id/in/produk/dekorasi/jam"
    product_links = get_all_links(main_url)
    for product in product_links:
        print(product)
        product_parse = parse_product(product)
        print(product_parse)
        break
    
