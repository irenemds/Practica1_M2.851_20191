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
    html_content = get_HTML(url)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
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

def get_all_book_info (book_url):
    returnValue = {}
    html_content = get_HTML(book_url)
    soup = BeautifulSoup(html_content, 'html.parser')
    book_info = soup.find("div", class_="libro_info")
    author = book_info.div.h3.small.string
    average_score = book_info.find("div", class_="estadisticas").span.string
    returnValue["Autor"] = author
    returnValue["Puntuacion"] = average_score

    card_info = book_info.find("div", class_="card")
    card_objects = card_info.find("li")
    first_card_object = card_objects.find("span")
    first_card_value = card_objects.find("a")
    returnValue[first_card_object.string] = first_card_value.string
    for nextSibling in card_objects.findNextSiblings():
        try:
            returnValue[nextSibling.find("span").string] = nextSibling.find("a").string
        except:
            aux_string = str(nextSibling)
            index_label = aux_string.find('</span>')+len('</span>')
            value = (aux_string[index_label:]).replace("</li>","").strip()
            returnValue[nextSibling.span.string] = value
    return returnValue

latest_releases = get_latest_releases(URL)
print (latest_releases)
for index, book in enumerate(latest_releases,start=0):
   book_info = get_all_book_info(book["URL"])
   latest_releases[index].update(book_info)
print(latest_releases)
#print (book_info)