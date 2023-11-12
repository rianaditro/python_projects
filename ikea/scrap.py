from requests_html import HTMLSession
from fake_useragent import UserAgent
ua = UserAgent()

url = "https://www.ikea.co.id/in/produk/dekorasi/jam"

session = HTMLSession()
session.headers.update({'User-Agent':ua.random})
r = session.get(url)
print(r.status_code)
r.html.render(sleep=1, timeout=10)
#get the product list from the xpath
product_links = r.html.absolute_links
print(product_links)#none
print(len(product_links))