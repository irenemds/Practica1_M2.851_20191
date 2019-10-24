def save_json_as_csv(list_dict_data):
    import csv
    csv_columns = set()
    for data in list_dict_data:
        for key in data.keys():
            csv_columns.add(key)
    csv_file = "info_libros_queleoahora.csv"
    try:
        with open(csv_file, 'w+', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list(csv_columns))
            writer.writeheader()
            for data in list_dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")