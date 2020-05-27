# coding=utf-8
import numpy as np


def game_core_v3(number):
    """Сначала устанавливаем любое random число, уменьшаем или увеличиваем его на половину диапазона поиска в
    зависимости от того, больше оно или меньше нужного, уменьшаем границу поиска. Функция принимает
    загаданное число и возвращает число попыток """
    count = 0
    predict = np.random.randint(1, 100)
    left = 1
    right = 100
    # left, right - границы поиска
    while number != predict:
        count += 1
        if number > predict:
            left = predict  # смещаем границу вправо
            predict = left + max(1, (right - left) // 2)
        elif number < predict:
            right = predict  # смещаем границу влево
            predict = right - max(1, (right - left) // 2)
    return count  # выход из цикла, если угадали


def score_game(game_core_v1):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_array = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_array.append(game_core_v1(number))
    score = int(np.mean(count_array))
    print("Ваш алгоритм угадывает число в среднем за " + str(score) + " попыток")
    return score


# Запускаем
score_game(game_core_v3)
