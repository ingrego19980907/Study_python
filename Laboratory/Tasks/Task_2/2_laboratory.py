
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

print(
    '\n\n\n\n\n___Завдання №1 Читати дані з таблиці Excel і заноситиме їх у DataFrame, переводячи їх у числові, '
    'та рахуватиме ентропію усієї сукупності грибів')


xlsx = pd.ExcelFile(r'C:\Python\Project\Study\Laboratory\Tasks\Task_1\Task_1.xlsx')


def stint(x):
    return ord(x) / 100.0


def stint1(x):
    return 1.0 if x == 'e' else 0.0


cols = list("ABCDEFGHIJKLMNOPQRSTUVW")

names = []
for i in cols:
    names.append(i * 2)

converters = {names[0]: stint1}
for i in names[1:]:
    converters.update({i: stint})

df = pd.read_excel(xlsx, usecols='A:W', header=None, names=names, nrows=50, converters=converters)

sorted_df = df.sort_values(by='AA')

sorted_df.to_excel('C:/Python/Project/Study/Laboratory/Tasks/Task_1/result_1.xlsx', header=False, index=False)

print(sorted_df)

# порахуємо кількість рядків у PE з різними значеннями
elem_count = df.shape[0]
print('elem_count=', elem_count, end='\n\n')

"""обчислимо ймовірності появи їстівних і отруйних грибів (частоти значень у першому стовпчику)
у батьківській групі і занесемо її до словника. Ключу "1"
відповідатиме ймовірність появи істівного гриба, а клчу
"0" - ймовірність появи отруйного"""

dict_probability = df['AA'].value_counts() / elem_count
MainEntropy = -dict_probability[0] * math.log(dict_probability[0]) - dict_probability[1] * math.log(dict_probability[1])
print("Виводимо словник ймовірностей! \n", dict_probability, end='\n\n')

# # Створюємо словник вловників, в якому ключами будуть значення, а елементами кількість об'єктів в кожній групі
list_of_dicts_val_and_qunt = []
for i in sorted_df[1:]:
    dict_value_and_quant = df[i].value_counts()
    list_of_dicts_val_and_qunt.append(dict_value_and_quant)

print('список словників =\n', list_of_dicts_val_and_qunt, end='\n\n')


# Створюємо список списків ключів словників
list_of_lists_keys_of_dicts = []
for dict in list_of_dicts_val_and_qunt:
    keys_list = []
    for key in dict.keys():
        keys_list.append(key)
    list_of_lists_keys_of_dicts.append(keys_list)

print('list_of_lists_keys_of_dicts\n', list_of_lists_keys_of_dicts, end='\n\n')

# list Кількості груп
list_of_ngroup = []
for list_keys in list_of_lists_keys_of_dicts:
    ngroup = len(list_keys)
    list_of_ngroup.append(ngroup)
print('list_of_ngroup\n', list_of_ngroup, end='\n\n')

# # Створюємо список кількостей елементів у кожній групі

list_of_lists_nig = []
for dict in list_of_dicts_val_and_qunt:
    value_list = []
    for key in dict.keys():
        value_list.append(dict[key])
    list_of_lists_nig.append(value_list)

print('list_of_lists_nig\n', list_of_lists_nig, end='\n\n')

# Середнє значення
list_average_values = []
for k in range(len(list_of_lists_keys_of_dicts)):
    average_value = 0.
    for i in range(len(list_of_lists_keys_of_dicts[k])):
        average_value += list_of_lists_keys_of_dicts[k][i] * list_of_lists_nig[k][i] / elem_count
    list_average_values.append(round(average_value, 3))
print('average value\n', list_average_values, end='\n\n')


list_of_dicts_namecol_aver_val = []
for av in list_average_values:
    VaV = {}
    for col in names:
        VaV.update({col: av})
    list_of_dicts_namecol_aver_val.append(VaV)
print('list_of_dicts_namecol_aver_val')
for dict in list_of_dicts_namecol_aver_val:
    print(dict)




print('\n\n\n\n\n___Завдання №2 Рахуватиме прирости інформації для усіх нецільових атрибутів грибів.')


print('\n\n\n\n\n___Завдання №3 За будь-якими 25 грибами таблиці будуватиме класифікаційні дерева для одного –двадцяти'
      'найбільш інформативних параметрів.')

print('\n\n\n\n\n___Завдання №4 Застосовуватиме класифікаційні дерева до решти 25 грибів. Для кожного класифікаційного'
      'дерева вираховуватиме кількість помилок класифікації решти 25 грибів та будуватиме'
      'залежність кількості помилок від розміру класифікаційного дерева. ')

print('\n\n\n\n\n___Завдання №5 Будуватиме класифікаційні моделі на основі перцептрона Розенблата.'
      'Застосувати модель для 25 грибів на двох атрибутах та двох алгебраїчних комбінаціях сукупності атрибутів. '
      'Перевірити роботу моделей на решті 25 грибах.')
