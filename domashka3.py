import numpy as np
import pandas as pd

## 1. Привести различные способы задания обьектов типа Series

# - списки(из python) или массивы (из Numpy)

# list = [1,2,3,4,5]
# a = np.arange(6, 11)

# print(pd.Series(list))
# print(pd.Series(a))

# # - скалярные значения

# const = 7
# print(pd.Series(const, index = [1,2,3]))

# # - словари

# dict = {'key1' : 'value1',
#         'key2' : 'value2',
#         'key3' : 'value3',
#         'key4' : 'value4',
#         'key5' : 'value5'}

# print(pd.Series(dict))

## 2. Привести различные способы создания обьектов типа DataFrame
# - через обьекты Series

# s1 = pd.Series([1, 2, 3, 4])
# s2 = pd.Series(["a", "b", "c", "d"])

# df1_2 = pd.DataFrame({"s1": s1, "s2": s2})
# print(df1_2)

# - списки словарей
# dict1 = {"key11": "value11", "key12": "value12", "key13": "value13"}

# dict2 = {"key11": "value21", "key12": "value22", "key13": "value23"}

# dict3 = {"key11": "value31", "key12": "value32", "key13": "value33"}

# list_of_dicts = [dict1, dict2, dict3]

# df_dictlist = pd.DataFrame(list_of_dicts)
# print(df_dictlist)

# - словари обьектов Series

s_dict1 = pd.Series(
    ["val1", "val2", "val3", "val4"], index=["key1", "key2", "key3", "key4"]
)
s_dict2 = pd.Series(
    ["val12", "val22", "val32", "val42"], index=["key1", "key2", "key3", "key4"]
)

df_s_dict = pd.DataFrame({"s_dict1": s_dict1, "s_dict2": s_dict2})

# print(df_s_dict)

# - двумерный массив Numpy

mas = np.arange(12).reshape(3, -1)
df_mas = pd.DataFrame(mas)
# print(df_mas)

# - структурированный массив Numpy

data = np.zeros(4, dtype={"names": ("name", "age"), "formats": ("U10", "i4")})

name = ["name1", "name2", "name3", "name4"]
age = [10, 20, 30, 40]

data["name"] = name
data["age"] = age

df_data = pd.DataFrame(data)
# print(df_data)

## 3. Обьедините 2 обьекта Series с неодинаковыми множествами ключей так, чтобы вместо NaN было 1

s11 = pd.Series(["a", "b", "c", "d"], index=[1, 2, 3, 4])
s22 = pd.Series(["aa", "bb", "cc", "dd", "ee"], index=[5, 6, 7, 8, 9])

df_s11_s22 = pd.DataFrame({"s11": s11, "s22": s22})
# print(df_s11_s22.fillna(1))

## 4. Переписать пример с транслированием для DataFrame так, чтобы вычитание происходило не по строкам,
#  а по СТОЛБЦАМ

a = np.arange(12)
a = a.reshape(3, 4)
df_a = pd.DataFrame(a)
print(a)
print((df_a.T - df_a.iloc[:, 0].T).T)

# 5. На примере объектов DataFrame
#  продемонстрируйте использование методов ffill() и bfill()

df = pd.DataFrame(
    [
        [np.nan, 2, np.nan, 0],
        [3, 4, np.nan, 1],
        [np.nan, np.nan, np.nan, np.nan],
        [np.nan, 3, np.nan, 4],
    ],
    columns=list("ABCD"),
)
print(df)

print(df.ffill())
print(df.bfill())
