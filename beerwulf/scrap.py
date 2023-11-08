from requests_html import HTMLSession
from bs4 import BeautifulSoup
import json

url = "https://www.beerwulf.com/en-gb/c/all-beers?segment=Beers&catalogCode=Beer_1"

session = HTMLSession()
#getting all url in a page
"""r = session.get(url)
r.html.render(sleep=1,scrolldown=15)
#return 83 links
links = r.html.xpath('//*[@id="product-items-container"]', first = True).absolute_links
"""

link = "https://www.beerwulf.com/en-gb/p/beers/newcastle-brown-ale-2l-keg"
r = session.get(link)
text = r.html.render(sleep=1)
text = r.html.html

"""with open("beerwulf.html","w") as file:
    file.writelines(text)"""

soup = BeautifulSoup(text,"html.parser")
script = soup.find("script",{"type":"application/ld+json"}).text.strip()
json_script = json.loads(script)
print(json_script['offers'])