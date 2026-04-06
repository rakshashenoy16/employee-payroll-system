import csv

def log_error(errors, file_path):
    if not errors:
        return
    
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["error", "record"])
        writer.writeheader()
        writer.writerows(errors)