from requests_html import HTMLSession

url = "https://www.beerwulf.com/en-gb/c/all-beers?segment=Beers&catalogCode=Beer_1"

session = HTMLSession()
r = session.get(url)
print(r.status_code)
r.html.render(sleep=1, scrolldown=15)
links = r.html.xpath('//*[@id="product-items-container"]', first=True).absolute_links
print(len(links))
print(links)

