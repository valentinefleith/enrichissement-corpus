import csv
from typing import List, Tuple


def write_to_csv(annotation: List[Tuple]):
    with open("annotation_manuelle.csv", "w", encoding="UTF-8") as csvfile:
        writer = csv.writer(csvfile)
        for tag in annotation:
            writer.writerow(tag)


def load_manual(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile)
        tags = [row for row in reader]
    return tags
