#!/usr/bin/env python

""" Este modulo contiene la funciones para actualizar la puntuación
    de los libros almacenados en el dataset.

    Esto se realizará periódicamente para mantener la información
    actualizada.
"""

__author__ = "Irene MS"
__credits__ = ["quelibroleo.com"]
__version__ = "1.0.1"

from Web_Scraping import get_updated_score
from csv_files import open_csv_as_json,save_json_as_csv

def main():
    #Se abre el fichero csv en formato json
    books_dict = open_csv_as_json()
    #Para cada libro se consulta la puntuación y se almacena.
    for index, book in enumerate(books_dict,start=0):
        books_dict[index]["Puntuacion"] = get_updated_score(book["URL"])
    save_json_as_csv(books_dict)

if __name__ == '__main__':
    main()