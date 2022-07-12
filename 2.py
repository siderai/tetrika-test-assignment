from collections import defaultdict
from typing import Dict, List
import re

import requests


url = "https://ru.wikipedia.org/w/api.php"

params = {
    "action": "query",
    "format": "json",
    "list": "categorymembers",
    "cmtitle": "Категория:Животные по алфавиту",
    "cmlimit": "max",
}

animals = []


def get_animals_list(url: str, params: Dict[str, str]) -> None:
    """Делает запросы к Wikipedia API, получает названия статей из категории "Животные по алфавиту"
    и складывает их в список animals.
    Примечания:
    1. За один запрос API выдает максимум 500 названий, а всего статей в категории ~ 40к,
    поэтому нужно выполнить ~ 80 запросов. Начиная со второго запроса используется рекурсия.
    Управление пагинацией происходит через параметр cmcontinue.
    2. В категории "Животные" русской Википедии есть названия на латинице
    (напр., названия одноклеточных). Чтобы соответствовать примеру (Перламутровый лосось),
    из выборки они исключены.
    3. Цикл отрабатывает за 20-25 секунд.
    """
    response = requests.get(url=url, params=params)
    data = response.json()

    pages = data["query"]["categorymembers"]
    for page in pages:
        animal_title = page["title"]
        if is_cyrillic(animal_title):
            animals.append(animal_title)

    if data.get("continue", None):
        params["cmcontinue"] = data["continue"]["cmcontinue"]
        # иллюстрация рекурсивной работы с api в рантайме:
        # print(params)
        # print("recursive step")
        get_animals_list(url, params)


def is_cyrillic(title):
    return bool(re.search("[а-яА-Я]", title[0]))


def count_animals_by_first_letter(animals: List[str]) -> None:
    """Принимает на вход список животных, для каждой буквы алфавита выводит число животных,
    название которых с нее начинается.
    A: 3020
    Б: 2231
    ...
    Я: 209"""
    counter = defaultdict(int)
    for animal in animals:
        first_letter = animal[0]
        counter[first_letter] += 1

    for char, count in sorted(counter.items()):
        print(f"{char.upper()}: {count}")


if __name__ == "__main__":
    get_animals_list(url, params)
    count_animals_by_first_letter(animals)
