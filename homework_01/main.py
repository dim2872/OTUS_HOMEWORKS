"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(data):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in data]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(data, flag):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def filter_numbers(data, flag):
        """
        функция, которая на вход принимает список из целых чисел,
        и возвращает только чётные/нечётные/простые числа
        (выбор производится передачей дополнительного аргумента)

        #>>> filter_numbers([1, 2, 3], ODD)
        <<< [1, 3]
        #>>> filter_numbers([2, 3, 4, 5], EVEN)
        <<< [2, 4]
        """
        if flag == ODD:
            return [number for number in data if number % 2 != 0]
        elif flag == EVEN:
            return [number for number in data if number % 2 == 0]
        elif flag == PRIME:
            return prime_numbers(data)

    def prime_numbers(data):
        lst = []
        for i in range(len(data)):
            for a in range(2, data[i]):
                if (data[i] % a) == 0:
                    break
                elif (data[i] // a) == 1:
                    lst.append(data[i])
                    break
        return lst
