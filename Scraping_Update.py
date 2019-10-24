from Web_Scraping import get_updated_score
from csv_files import open_csv_as_json

books_dict = open_csv_as_json()
for index, book in enumerate(books_dict,start=0):
    book["Puntuacion"] = get_updated_score(book["URL"])

