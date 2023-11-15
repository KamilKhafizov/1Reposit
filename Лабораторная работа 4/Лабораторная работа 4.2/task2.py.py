# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, newline='') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')

        headers = next(csv_reader)

        data = []


        for row in csv_reader:
            row_dict = {headers[i]: row[i] for i in range(len(headers))}

            data.append(row_dict)

    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
