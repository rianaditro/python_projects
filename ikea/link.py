from requests_html import HTMLSession

url = "https://www.ikea.co.id/in/produk/dekorasi/jam"

session = HTMLSession()
r = session.get(url)
r.html.render(sleep=1)
link = r.html.xpath('//*[@id="product-list-component"]/div[4]/div', first=True).absolute_links
print(len(link))
