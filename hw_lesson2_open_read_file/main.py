# import os
from pprint import pprint

cook_book = {} # Создали словарь
# Открываем файл на чтение
with open('recipes.txt', encoding='utf-8') as file: 
    for line in file:
        name_of_dish = line.strip()
        ingredient_count = file.readline()
        ingredient = []
        for i in range(int(ingredient_count)):
            ing = file.readline()
            ingredient_name, quantity, measure = ing.strip().split(' | ')
            ingredient.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[name_of_dish] = ingredient
    pprint(cook_book)