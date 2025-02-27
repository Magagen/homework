import numpy as np
import pandas as pd

# задание 1 разобраться как использовать мультииндексные ключи в конкретном примере

index = [
    ("city_1", 2010, 1),
    ("city_1", 2010, 2),
    ("city_1", 2020, 1),
    ("city_1", 2020, 2),
    ("city_2", 2010, 1),
    ("city_2", 2010, 2),
    ("city_2", 2020, 1),
    ("city_2", 2020, 2),
    ("city_3", 2010, 1),
    ("city_3", 2010, 2),
    ("city_3", 2020, 1),
    ("city_3", 2020, 2),
]

population = [101, 1010, 201, 2010, 102, 1020, 202, 2020, 103, 1030, 203, 2030]
index = pd.MultiIndex.from_tuples(index)
pop = pd.Series(population, index=index)


pop_df = pd.DataFrame(
    {"total": pop, "something": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]}
)

# print(pop_df['something']['city_1'])
# print(pop_df['something'][['city_1','city_3']])
# print(pop_df.loc[['city_1', 'city_3'] ][['total','something']])

# задание 2: из данных выбрать данные по
index = pd.MultiIndex.from_product(
    [
        ["city_1", "city_2"],
        [2010, 2020],
    ],
    names=["city", "year"],
)


columns = pd.MultiIndex.from_product(
    [["person_1", "person_2", "person_3"], ["job_1", "job_2"]], names=["worker", "job"]
)

rng = np.random.default_rng(1)
data = rng.random((4, 6))

data_df = pd.DataFrame(data, index=index, columns=columns)
# print(data_df)

# - 2020 году (для всех столбцов)
# print()
# print()
# print()
idx = pd.IndexSlice
# print(data_df.loc[idx[:, 2020], idx[:]]) ## можно print(data_df.loc[idx[:, 2020], :])

# - job_1 (для всех строк)

# print(data_df.loc[idx[:], idx[:, 'job_1']]) ## можно  print(data_df.loc[:, idx[:, 'job_1']])

# - # - для city_1 и job_2

# print(data_df.loc[idx['city_1', :], idx[:, 'job_2']])


## задание 3: взяв за основу DataFrame

index = pd.MultiIndex.from_product(
    [["city_1", "city_2"], [2010, 2020]], names=["city", "year"]
)
columns = pd.MultiIndex.from_product(
    [["person_1", "person_2", "person_3"], ["job_1", "job_2"]], names=["worker", "job"]
)


# Выполнить запрос на получение следующих данных

# - все данные по person_1 и person_3
# print(data_df.loc[idx[:], idx[('person_1','person_3'),:]])

# - все данные по 'city_1' и первым двум 'person'

# print(data_df.loc[idx['city_1', :], idx[('person_1','person_2'),:]])

# Приведите пример с использванием pd.IndexSlice

# print(data_df.loc[idx[:], idx[('person_1','person_3'),:]])

# задание 4: привести пример использования inner и outer джойнов для Series

# df3 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']])
# df1 = pd.DataFrame([['a', 1], ['b', 2]])
# print(pd.concat([df1, df3], join='inner'))
