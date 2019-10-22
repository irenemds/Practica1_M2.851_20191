import requests
from bs4 import BeautifulSoup

def get_HTML(url="https://api.github.com"):
    returnValue = None
    response = requests.get(url)
    if response.status_code == 200:
        returnValue = response.content
    return returnValue



URL = "http://quelibroleo.hola.com/novedades"
HTML = get_HTML(URL)
if HTML:
    soup = BeautifulSoup(HTML, 'html.parser')
    #print(soup.prettify())
    items = soup.find_all("div", class_="item")

    for item in items:
        item_info = item.find("div", class_ = "col-lg-8 col-xs-12")
        print (item_info)