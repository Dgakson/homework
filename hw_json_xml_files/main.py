# Вам дан json-файл с новостями. 
# Вам дан xml-файл с новостями. 
# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов.

##  Используй метод Counter(word).most_common(10)

import json
import xml.etree.ElementTree as ET
from pprint import pprint
from collections import Counter


def read_json(file_path, word_max_len=6, top_words_amt=10):
    """
    функция для чтения json_файла с новостями.
    """
    all_word = []
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        items = data['rss']['channel']['items']

    for description in items:
    # Здесь выводится текст description
        word = description['description'].split()
        for w in word:
            if len(w) > word_max_len:
                all_word.append(w)

    # top_word = Counter(all_word).most_common(top_words_amt)
    result = [t[0] for t in Counter(all_word).most_common(top_words_amt)]
    return result

def read_xml(file_path, word_max_len=6, top_words_amt=10):
    """
    функция для чтения xml с новостями.
    """
    all_word = []
    #Открытие файла xml на чтение и
    tree = ET.parse(file_path)
    root = tree.getroot()
    description = root.findall('channel/item/description')
    for d in description:
        word = d.text.split()
        for w in word:
            if len(w) > word_max_len:
                all_word.append(w)

    result = [t[0] for t in Counter(all_word).most_common(top_words_amt)]
    return result

# print(read_json("newsafr.json"))
print(read_xml("newsafr.xml"))