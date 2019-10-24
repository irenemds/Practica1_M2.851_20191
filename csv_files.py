import csv
csv_file = "info_libros_queleoahora.csv"

def save_json_as_csv(list_dict_data):
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
    returnValue = None
    with open(csv_file) as f:
        returnValue = [{k: v for k, v in row.items()}
             for row in csv.DictReader(f, skipinitialspace=True)]
    return returnValue