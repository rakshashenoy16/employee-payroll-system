import csv
#loads csv files
def load_csv(file_path):
    with open(file_path, newline='') as file:
        return list(csv.DictReader(file))