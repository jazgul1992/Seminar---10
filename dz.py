# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
#  Ваша задача перевести его в one hot вид. Надо это сделать без get_dummies. И надо сделать это без циклов.


import pandas as pd
import numpy as np
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)

data['tmp'] = 1
data.set_index([data.index, 'whoAmI'], inplace = True)
data = data.unstack(level =- 1, fill_value = 0).astype(int)
data.columns.name = None
print(data)