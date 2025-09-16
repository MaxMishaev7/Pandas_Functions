"""
Напишите функцию, которая классифицирует фильмы из материалов
занятия по правилам:
 - оценка 2 и ниже - низкий рейтинг
 - оценка 4 и ниже - средниий рейтинг
 - оценка 4,5 и 5 - высокий рейтинг
Результат классификации: столбец class
"""

import pandas as pd

def ratings(rating):
    if (rating <= 2 ):
        return "низкий рейтинг"
    elif (rating <= 4):
        return "средний рейтинг"
    elif (rating == 4.5 or rating == 5):
        return "высокий рейтинг"
    return "undefined"

data_frame = pd.read_csv('ratings.csv')
print(data_frame.head(10))
data_frame['class'] = data_frame['rating'].apply(ratings)
print(data_frame.head(10))


