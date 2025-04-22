"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np

def random_predict_v4(number:int=1) -> int:
    """Рандомно угадываем число
    

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    
    
    count = 0
    # присваиваем значение, соответствующее нижней и верхней границе диапазона поиска
    start = 1  
    stop = 101

    while True:
        count += 1
        guess = np.mean([start, stop]).astype(int)  # находим середину диапазона
        if guess == number:
            break
        # Если не угадали, перезаписываем start или stop
        elif guess < number:
            start = guess
        else:
            stop = guess
            
    return (count)  

print(f'Количество попыток: {random_predict_v4()}') 

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм
    

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
        
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
   
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


# RUN
if __name__ == '__main__':  
    score_game(random_predict_v4)