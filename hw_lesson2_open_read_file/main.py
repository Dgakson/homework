# import os
from pprint import pprint

def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = int(ingredient['quantity']) * person_count
                measure = ingredient['measure']
                
                if ingredient_name in shopping_list:
                    shopping_list[ingredient_name]['quantity'] += quantity
                else:
                    shopping_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
    return shopping_list


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
    # pprint(cook_book)

print('--------')
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shopping_list = get_shop_list_by_dishes(dishes, person_count)
pprint(shopping_list)
