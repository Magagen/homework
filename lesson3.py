import numpy as np
import pandas as pd


# Pandas - расширение Numpy (структурированные массивы). Строки и столбцы индексируются метками,
# а не только числовыми значениями

# Series, DataFrame, Index

## Series

# data = pd.Series([0.25, 0.5, 0.75, 1.0])
# print(data)
# print(type(data))

# print(data.values)
# print(type(data.values))

# print(data.index)
# print(type(data.index))

# data = pd.Series([0.25, 0.5, 0.75, 1.0])
# print(data[0])
# print(data[1:3])

# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
# print(data)
# print(data['a'])
# print(data['b':'d'])

# print(type(data.index))

# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=[1, 10, 7, 'd'])
# print(data)

# print(data[1])
# print(data[10:'d'])

# population_dict = {
#     'city1': 1001,
#     'city2': 1002,
#     'city3': 1003,
#     'city4': 1004,
#     'city5': 1005,
# }

# population = pd.Series(population_dict)
# print(population)

# print(population['city4'])
# print(population['city4':'city5'])

# Для создания Series можно использовать
# - списки(из python) или массивы (из Numpy)
# - скалярные значения
# - словари
## 1. Привести различные способы задания обьектов типа Series

## DataFrame - двумерный массив с явно определенными индексами.
# Последовательность "согласованных" обьектов Series

# population_dict = {
#     'city1': 1001,
#     'city2': 1002,
#     'city3': 1003,
#     'city4': 1004,
#     'city5': 1005,
# }

# area_dict = {
#     'city1': 9991,
#     'city2': 9992,
#     'city3': 9993,
#     'city4': 9994,
#     'city5': 9995,
# }

# population = pd.Series(population_dict)
# area = pd.Series(area_dict)

# # print(population)
# # print(area)

# states = pd.DataFrame({
#     'population1': population,
#     'area1': area,
# })

# print(states)

# print(states.values)
# print(states.index)
# print(states.columns)

# print(type(states.values))
# print(type(states.index))
# print(type(states.columns))

# print(states['area1'])


# DataFrame. Спобы создания
# - через обьекты Series
# - списки словарей
# - словари обьектов Series
# - двумерный массив Numpy
# - структурированный массив Numpy
## 2. Привести различные способы создания обьектов типа DataFrame

# Index - способ организации ссылки на данные обьектов Series и DataFrame.
# Index - неизменяем, упорядочен, является мультимножеством(могут быть повторяющиеся значения)

# ind = pd.Index([2,3,5,7,11])
# print(ind[1])
# print(ind[::2])

# ind[1] = 5 # незя

# Index - следует соглашениям обьекта set (python)
# indA = pd.Index([1,2,3,4,5])
# indb = pd.Index([2,3,4,5,6])

# print(indA.intersection(indb))

# # Выборка данных из Series (как словарь (python))

# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])

# print('a' in data)
# print('z' in data)

# print(data.keys())

# print(list(data.items()))

# data['a'] = 100
# data['z'] = 1000

# print(data)


## как одномерный массив

# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])

# print(data['a':'c'])
# print(data[0:2])  # не отменяется стандартная адресация
# print(data[(data > 0.5) & (data < 1)])
# print(data[['a', 'd']])


# # атрибуты-индексаторы
# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=[1, 3, 10, 15])

# print(data[1])

# print(data.loc[1]) # индекс заданный [1, 3, 10, 15]
# print(data.iloc[1]) # индекс стандартный

# Выборка данных из DataFrame
# как словарь

# population_dict = {
#     "city1": 1001,
#     "city2": 1002,
#     "city3": 1003,
#     "city4": 1004,
#     "city5": 1005,
# }

# area_dict = {
#     "city1": 9991,
#     "city2": 9992,
#     "city3": 9993,
#     "city4": 9994,
#     "city5": 9995,
# }

# pop = pd.Series(
#     {
#         "city1": 1001,
#         "city2": 1002,
#         "city3": 1003,
#         "city4": 1004,
#         "city5": 1005,
#     }
# )

# area = pd.Series(
#     {
#         "city1": 9991,
#         "city2": 9992,
#         "city3": 9993,
#         "city4": 9994,
#         "city5": 9995,
#     }
# )

# data = pd.DataFrame({"area1":area, 'pop1':pop, 'pop':pop})
# # print(data)

# print(data['area1'])
# print(data.area1)

# print(data.pop1 is data['pop1'])
# print(data.pop is data['pop'])

# data['new'] = data['area1']
# data['new1'] = data['area1']/data['pop1']

# print(data)

# Двумерный Numpy-массив
# data = pd.DataFrame({"area1": area, "pop1": pop, "pop": pop})

# print(data)

# print(data.values)

# print(data.T)

# print(data['area1'])

# print(data.values[0])  # чтобы к строке обратиться

# print(data.values[0:3])

# атрибуты-индексаторы

# print(data)
# print(data.iloc[:3, 1:2])
# print(data.loc[:"city4", "pop1":"pop"])
# print(data.loc[data['pop'] > 1002, ["area1", "pop"]])

# data.iloc[0, 2] = 999999

# print(data)

# rng = np.random.default_rng()
# s = pd.Series(rng.integers(0, 10, 4))

# print(s)
# print(np.exp(s))

# pop = pd.Series(
#     {
#         "city1": 1001,
#         "city2": 1002,
#         "city3": 1003,
#         "city41": 1004,
#         "city51": 1005,
#     }
# )

# area = pd.Series(
#     {
#         "city1": 9991,
#         "city2": 9992,
#         "city3": 9993,
#         "city42": 9994,
#         "city52": 9995,
#     }
# )

# data = pd.DataFrame({"area1": area, "pop1": pop})
# print(data)
# NaN - not a number

## 3. Обьедините 2 обьекта Series с неодинаковыми множествами ключей так, чтобы вместо NaN было 1

# rng = np.random.default_rng()
# dfA = pd.DataFrame(rng.integers(0, 10, (2,2)), columns=['a', 'b'])
# dfB = pd.DataFrame(rng.integers(0, 10, (3,3)), columns=['a', 'b', 'c'])

# print(dfA)
# print(dfB)

# print(dfA + dfB)

# rng = np.random.default_rng(1)

# A = rng.integers(0, 10, (3, 4))
# # print(A)

# # print(A[0])

# # print(A - A[0])

# df = pd.DataFrame(A, columns=["a", "b", "c", "d"])
# print(df)

# print(df.iloc[0])

# print(df - df.iloc[0])

# print(df.iloc[0, ::2])

# print(df - df.iloc[0, ::2])

## 4. Переписать пример с транслированием для DataFrame так, чтобы вычитание происходило не по строкам,
#  а по СТОЛБЦАМ


# NaN - not a number

# NA - значения: NaN, null

# Pandas. Два способа хранения отсутствующих значений
# индикаторы Nan, None
# null

# None - обьект (накладные расходы). Не работает с sum, min и др

# vall = np.array([1, 2, 3])
# print(vall.sum())

# vall = np.array([1, None, 2, 3])
# print(vall.sum())

# vall = np.array([1, np.nan, 2, 3])
# print(vall)
# print(vall.sum())
# print(np.sum(vall))
# print(np.nansum(vall))


# x = pd.Series(range(10), dtype=int)
# print(x)

# x[0] = None
# x[1] = np.nan

# print(x)

# x1 = pd.Series(["a", "b", "c"])
# print(x1)

# x1[0] = None
# x1[1] = np.nan

# print(x1)

# #

# x2 = pd.Series([1, 2, 3, np.nan, None, pd.NA])
# print(x2)

# x3 = pd.Series([1, 2, 3, np.nan, None, pd.NA], dtype="Int32")
# print(x3)

# print(x3.isnull())
# print(x3[x3.isnull()])
# print(x3[x3.notnull()])

# print(x3.dropna())

df = pd.DataFrame(
    [
        [1, 2, 3, np.nan, None, pd.NA],
        [1, 2, 3, None, 5, 6],
        [1, np.nan, 3, None, np.nan, 6],
    ]
)

print(df)
# print(df.dropna())
# print('dddddddddddddd')
# print(df.dropna(axis=0))
# print(df.dropna(axis=1))

# how =
# all - все значения NA
# any - хоть одно NA

# thresh = x, остается, если присутствует МИНИМУМ х НЕПУСТЫХ значений

print(df.dropna(axis=1, how="all"))
print(df.dropna(axis=1, how="any"))
print(df.dropna(axis=1, thresh=2))

## 5. На примере обьектов DataFrame продемонстрируйте использование методов ffill() и bfill()
