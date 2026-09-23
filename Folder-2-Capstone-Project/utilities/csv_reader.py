import csv


class CSVReader:

    @staticmethod
    def read_products(file_path):

        products = []

        with open(file_path, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:
                products.append(row["product"])

        return products