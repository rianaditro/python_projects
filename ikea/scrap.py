from requests_html import HTMLSession

def access(url):
    session = HTMLSession()
    r = session.get(url)
    return r

def get_all_links(main_url):
    r = access(main_url)
    product_links = r.html.xpath('//*[@id="product-list-component"]/div[4]/div',first = True).absolute_links
    return product_links

def parse():
    None

if __name__=="__main__":
    main_url = "https://www.ikea.co.id/in/produk/dekorasi/jam"
    product_links = get_all_links(main_url)
    print(len(product_links))