from requests_html import HTMLSession
from bs4 import BeautifulSoup

def access(url):
    session = HTMLSession()
    r = session.get(url)
    r.html.render(sleep=1)
    return r

def get_all_links(main_url):
    r = access(main_url)
    product_links = r.html.xpath('//*[@id="product-list-component"]/div[4]/div', first=True).absolute_links
    return product_links

def parse_per_product(product_url):
    r = access(product_url)
    soup = BeautifulSoup(r.html.html,"html.parser")
    name = parse("div","d-flex flex-row",soup)

    result = {"product name":name,
              "url":product_url}
    return result

def parse(tag, class_,soup):
    data = soup.find(tag,class_).get_text().strip
    return data

if __name__=="__main__":
    main_url = "https://www.ikea.co.id/in/produk/dekorasi/jam"
    product_links = get_all_links(main_url)
    for product in product_links:
        product_parse = parse_per_product(product)
        print(product_parse)
        break
    
