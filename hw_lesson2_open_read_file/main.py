from pprint import pprint

def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for dish in dishes:
        if dish in cook_book:  # проверяем, что название блюда есть в книге рецептов
            for ingredient in cook_book[dish]:  # проходим циклом по ингридиентам конкретного блюда
                ingredient_name = ingredient['ingredient_name']
                quantity = int(ingredient['quantity']) * person_count
                measure = ingredient['measure']
                
                # Если уже есть, то добавляем, если нет, то заводим 
                if ingredient_name in shopping_list:
                    shopping_list[ingredient_name]['quantity'] += quantity
                else:
                    shopping_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
    return shopping_list


cook_book = {} # Создали словарь(книгу) рецептов
# Открываем файл на чтение
with open('recipes.txt', encoding='utf-8') as file: 
    for line in file:
        name_of_dish = line.strip()  # из первой строки получили название блюда
        ingredient_count = file.readline() # перепргнули на след.строки и присвоили значение в переменную
        ingredient = []     #  создали список ингридентов
        for i in range(int(ingredient_count)):  # проходим циклом по ингридентам и добавляем их в список
            ing = file.readline()
            ingredient_name, quantity, measure = ing.strip().split(' | ')  # делим строчку по символу верт.черты
            ingredient.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[name_of_dish] = ingredient    # добавили список ингридентов в словарь рецептов
    # pprint(cook_book)

print('--------')

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2

shopping_list = get_shop_list_by_dishes(dishes, person_count)
pprint(shopping_list)
