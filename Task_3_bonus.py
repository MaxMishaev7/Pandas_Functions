"""
Задание 3 (бонусное)

Есть мнение, что раньше снимали настоящее кино, не то что сейчас. 
Ваша задача — проверить это утверждение, используя файлы с рейтингами фильмов 
из прошлого домашнего занятия: 

файл movies.csv и ratings.csv из базы. 

Нужно проверить, верно ли, что с ростом года выпуска фильма его средний рейтинг становится ниже.

Вы не будете затрагивать субьективные факторы выставления этих рейтингов, 
а пройдётесь по алгоритму:

1. В переменную years запишите список из всех годов с 1950 по 2010 года.

2. Напишите функцию production_year, которая каждой строке из названия фильма 
выставляет год выпуска (столбец year). 

Не все названия фильмов содержат год выпуска в одинаковом формате, поэтому используйте алгоритм:

a) для каждой строки пройдите по всем годам списка years;
b) если номер года присутствует в названии фильма, то функция возвращает этот год, 
   как год выпуска;
c) если ни один из номеров года списка years не встретился в названии фильма, 
   то возвращается 1900 год.
   
Запишите год выпуска фильма по алгоритму пункта 2 в новый столбец ‘year’.

Посчитайте средний рейтинг всех фильмов для каждого значения столбца ‘year’ и отсортируйте результат по убыванию рейтинга.
"""

import re
import pandas as pd


def production_year(film_name):
   year_int_lst = list(range(1950, 2011))
   year_str_lst = []
   for year_int in year_int_lst:
      year_str_lst.append(str(year_int))
   res = re.search('\d{4}', film_name)
   if res == None or res.group() not in year_str_lst:
      return '1900'
   year_str = res.group()
   if year_str in year_str_lst: 
      return year_str
   

def groupby_function(data):
   return data['rating'].mean()

df = pd.read_csv('movies.csv')
df['year'] = df['title'].apply(production_year)
print(df.tail(30))
ratings_df = pd.read_csv('ratings.csv')
joined_df_ratings = df.merge(ratings_df, on='movieId', how='left')
print(joined_df_ratings.head(50))

joined_df_ratings = joined_df_ratings.groupby(['year']).agg({'rating': 'mean'})
print(joined_df_ratings.reset_index().sort_values(by=['rating'], ascending=False).head(50))




