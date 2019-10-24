#!/usr/bin/env python

""" Este modulo contiene las funciones para manipular los ficheros csv
    y transformarlos de y a diccionario.
"""

__author__ = "Irene MS"
__credits__ = ["quelibroleo.com"]
__version__ = "1.0.1"

import csv
csv_file = "info_libros_queleoahora.csv"

def save_json_as_csv(list_dict_data):
    #Almacena los datos de diccionario en el fichero csv.
    csv_columns = set()
    for data in list_dict_data:
        for key in data.keys():
            csv_columns.add(key)
    try:
        with open(csv_file, 'w+', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list(csv_columns))
            writer.writeheader()
            for data in list_dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")

def open_csv_as_json():
    #Abre fichero csv en formato diccionario.
    returnValue = None
    with open(csv_file) as f:
        returnValue = [{k: v for k, v in row.items()}
             for row in csv.DictReader(f, skipinitialspace=True)]
    return returnValue