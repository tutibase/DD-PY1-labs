import json


def task() -> float:
    with open('input.json') as file:
        data = json.load(file)

    result = 0.
    for i in data:
        result += i['score'] * i['weight']
    return round(result, 3)


print(task())
