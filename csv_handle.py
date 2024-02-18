import csv
from typing import List, Tuple


def write_to_csv(annotation: List[Tuple]):
    with open("annotation_manuelle.csv", "w", encoding="UTF-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Mot", "POS"])
        for tag in annotation:
            writer.writerow(tag)
