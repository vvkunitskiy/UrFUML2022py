"""
Игра "Угадай число"
Компьютер загадывает число и сам отгадывает его менее чем за 20 попыток
"""

import numpy as np

# Задаём диапазон для загадывания числа от/до включительно
num_min = 0
num_max = 100


def smart_predict(number: int = 1) -> int:
    """Угадываем число, учитывая обратную связь о больше/меньше

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    left = num_min
    right = num_max + 1
    
    # print("Было загадано число:", number) # Раскомментить для наблюдения за процессом угадывания
    
    while True:
        count += 1
        
        predict_number = np.random.randint(left, right)  # предполагаемое число
        
        if predict_number > number:
            right = predict_number # сужаем границы поиска справа
            
            #print("Число", predict_number, "больше загаданного") # Раскомментить для наблюдения за процессом угадывания
        
        elif predict_number < number:
            left = predict_number + 1 # сужаем границы поиска слева
            
            #print("Число", predict_number, "меньше загаданного") # Раскомментить для наблюдения за процессом угадывания
        
        else:
            break  # выход из цикла если угадали
    
    #print("Компьютер удадал число", predict_number, "за", count, "попыток!") # Раскомментить для наблюдения за процессом угадывания
    
    return count


def score_game(smart_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        smart_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости (при необходимости)
    random_array = np.random.randint(num_min, num_max + 1 , size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(object)(smart_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

# RUN
score_game(smart_predict)