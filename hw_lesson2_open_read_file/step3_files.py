from pprint import pprint

files = ['1.txt', '2.txt', '3.txt']
service_info = []

# Считывание и подсчет строк
for filename in files:
    with open(filename, encoding='utf-8') as file:
        content = file.readlines()
        line_count = len(content)
        service_info.append((filename, line_count, content))

# Сортировка по количеству строк
service_info.sort(key=lambda x: x[1])  # лямбда-функция указывает, что сортировка должна происходить по второму элементу

# Запись в результующий файл
with open('result.txt', 'w', encoding='utf-8') as result:
    for filename, line_count, content in service_info:
        result.write(f'{filename}\n{line_count}\n')
        result.writelines(content)
        result.write('\n\n')
    print("Результирующий файл создан")
