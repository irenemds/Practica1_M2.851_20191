#!/usr/bin/env python

""" Este modulo contiene las principales funciones para realizar
    scraping y almacenadode la página seleccionada en la variable
    global URL. Utilizará funciones adicionales para el almacenado.
"""

__author__ = "Irene MS"
__credits__ = ["quelibroleo.com"]
__version__ = "1.0.1"

import requests
from bs4 import BeautifulSoup
from csv_files import save_json_as_csv

URL = "http://quelibroleo.hola.com/novedades"

def get_HTML(url):
    #Devuelve el código HTML de la página solicitada
    returnValue = None
    response = requests.get(url)
    if response.status_code == 200:
        #Se comprueba que la petición fue correcta.
        returnValue = response.content
    return returnValue

def get_latest_releases(url):
    #Obtiene los últimos estrenos de libros mostrados en la página solicitada.
    returnValue = None
    results = []
    html_content = get_HTML(url)
    if html_content:
        soup = BeautifulSoup(html_content, "html.parser")
        #Cada elemento está contenido en un "div" de clase "item"
        items = soup.find_all("div", class_="item")

        for item in items:
            #Se parsea el contenido de la página obteniendo título
            #y URL para información completa del libro.
            item_info = item.find("div", class_="col-lg-8 col-xs-12")
            title = item_info.a.string
            book_url = item_info.a.get("href")
            json_info = {"Titulo":title, "URL": book_url}
            results.append(json_info)
    else:
        raise Exception('Connection failed', url)

    returnValue = results
    return returnValue

def get_all_book_info (book_url):
    #Devuelve un diccionario con información adicional sobre el libro solicitado
    returnValue = {}

    html_content = get_HTML(book_url)
    soup = BeautifulSoup(html_content, 'html.parser')
    # Todos los elementos están contenidos en un "div" de clase "libro_info"
    book_info = soup.find("div", class_="libro_info")
    #Se parsean los atributos restantes.
    author = book_info.div.h3.small.string
    average_score = book_info.find("div", class_="estadisticas").span.string
    #Se incluyen los atributos en el diccionario.
    returnValue["Autor"] = author
    returnValue["Puntuacion"] = average_score
    #El resto de la información se encuentra en el objeto de la clase "card".
    card_info = book_info.find("div", class_="card")
    card_objects = card_info.find("li")
    #Los objetos son variables por lo que se utiliza la generación dinámica de los valores.
    first_card_object = card_objects.find("span")
    first_card_value = card_objects.find("a")
    returnValue[first_card_object.string] = first_card_value.string
    #Iteración sobre los objetos "li" de la tabla.
    for nextSibling in card_objects.findNextSiblings():
        try:
            #Se intenta parsear cada línea y se añade al diccionario
            returnValue[nextSibling.find("span").string] = nextSibling.find("a").string
        except:
            #Si el parseo con BeautifulSoup no funciona se hace mediante código.
            aux_string = str(nextSibling)
            index_label = aux_string.find('</span>')+len('</span>')
            value = (aux_string[index_label:]).replace("</li>","").strip()
            # Se añaden los valores al diccionario
            returnValue[nextSibling.span.string] = value
    return returnValue

def get_updated_score(book_url):
    #Obtiene el campo de la puntuación de la página de información de un libro-
    returnValue = None
    html_content = get_HTML(book_url)
    soup = BeautifulSoup(html_content, 'html.parser')
    book_info = soup.find("div", class_="libro_info")
    average_score = book_info.find("div", class_="estadisticas").span.string
    returnValue = average_score

    return returnValue

def main():
    latest_releases = get_latest_releases(URL)
    print (latest_releases)
    for index, book in enumerate(latest_releases,start=0):
       book_info = get_all_book_info(book["URL"])
       latest_releases[index].update(book_info)
    print(latest_releases)
    save_json_as_csv(latest_releases)

if __name__ == '__main__':
    main()