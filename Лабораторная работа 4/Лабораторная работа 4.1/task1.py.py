# TODO решите задачу
import json

def task() -> float:

        with open('input.json', 'r') as file:
            data = json.load(file)


        result_sum = sum(entry["score"] * entry["weight"] for entry in data)


        result_sum = round(result_sum, 3)

        return result_sum


print(task())

