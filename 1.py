from typing import List, Union


def task(array: Union[str, List[Union[str, int]]]) -> Union[int, None]:
    """Принимает на вход строки и массивы из строк и чисел. Учтены оба варианта, т.к. в задании указаны массивы,
    а в примере - строка. Возвращает индекс первого нуля в коллекции"""
    for i, value in enumerate(tuple(array)):
        if isinstance(value, str):
            num = int(value)
        else:
            num = value
        if num == 0:
            return i


# 11
print(task(["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0"]))
print(task(["1", "1", 1, "1", "1", "1", 1, "1", "1", "1", "1", 0, 0, "0"]))
print(task("111111111110000000000000000"))
