from typing import List, Union


def task(array: Union[str, List[Union[str, int]]]) -> Union[int, None]:
    for i, value in enumerate(tuple(array)):
        if isinstance(value, str):
            num = int(value)
        else:
            num = value
        if num == 0:
            return i


# принимает на вход строки и массивы из строк и чисел
# учел оба варианта, потому что в задании указаны массивы, а в примере - строка
print(task(["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0"]))
print(task(["1", "1", 1, "1", "1", "1", 1, "1", "1", "1", "1", 0, 0, "0"]))
print(task("111111111110000000000000000"))
