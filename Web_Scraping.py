import requests
from bs4 import BeautifulSoup

URL = "http://quelibroleo.hola.com/novedades"

def get_HTML(url):
    returnValue = None
    response = requests.get(url)
    if response.status_code == 200:
        returnValue = response.content
    return returnValue

def get_latest_releases(url):
    returnValue = None
    results = []
    HTML = get_HTML(URL)
    if HTML:
        soup = BeautifulSoup(HTML, 'html.parser')
        #print(soup.prettify())
        items = soup.find_all("div", class_="item")

        for item in items:
            item_info = item.find("div", class_ = "col-lg-8 col-xs-12")
            #print (item_info)
            title = item_info.a.string
            book_url = item_info.a.get('href')
            json_info = {"Titulo":title, "URL": book_url}
            results.append(json_info)

        returnValue = results
    return returnValue

    latest_releases = get_latest_releases(URL)


