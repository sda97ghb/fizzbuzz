"""
Тестовое задание.

Дано: Есть вербальная английская игра, FizzBuzz - два человека по очереди называют числа:
  - если число без остатка делится на 3, его заменяют на Fizz;
  - если число без остатка делится на 5, его заменяют на Buzz;
  - если делится без остатка и на 3, и на 5, число заменяют на FizzBuzz.
Есть вероятность, что через пару-тройку лет эти правила потребуется доработать.

Задача: Написать скрипт максимально возможного качества, содержащий функцию, которая принимает следующие аргументы:
  - (обязательный) лимит - до какого числа (включительно) нужно вывести всё, что могут сказать два игрока
  - (необязательный) вариант замены элементов в игре - вместо числа, которое без остатка делится на 4 было, например, "Argh", и вместо числа, которое делится на 7 - было, например, "Blergh"

Пример вывода скрипта с лимитом 16 и заменой чисел, кратных 3 на "Fizz", кратных 5 на "Buzz":
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
"""
from typing import Dict

DEFAULT_REPLACES = {3: "Fizz", 5: "Buzz"}


def find_replaces(n: int, replaces: Dict[int, str]):
    n_replaces = []
    for d, w in replaces.items():
        if n % d == 0:
            n_replaces.append(w)
    return n_replaces


def fizz_buzz(limit: int, replaces: Dict[int, str] = None):
    replaces = replaces if replaces is not None else DEFAULT_REPLACES
    for n in range(1, limit + 1):
        n_replaces = find_replaces(n, replaces)
        if n_replaces:
            yield "".join(n_replaces)
        else:
            yield str(n)


if __name__ == '__main__':
    for r in fizz_buzz(16):
        print(r)
