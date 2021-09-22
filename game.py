"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    n=1
    k=101
    while True:
        count += 1
        predict_number = (k+n)//2  # предполагаемое число. с каждым шагом количество возможных оставших чисел уменьшается в два раза.
     
        if number == predict_number:
            break  # выход из цикла, если угадали
        elif number > predict_number:
            n = predict_number
        elif number < predict_number:
            k = predict_number
        else:
             if number > (k-n)/2:
                 n=(k-n)/2
             else: k=(k-n)/2
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список Pчисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

if __name__ == "__main__":
    #RUN
    score_game(random_predict)
