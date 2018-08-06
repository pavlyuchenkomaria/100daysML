import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

if __name__ == '__main__':
    # pd.read_csv - мы вызываем функцию, которая берет наши данные
    # и создает объект типа dataframe
    read_csv = pd.read_csv('50_Startups.csv')
    # с помощью переменной iloc мы по индексам выбираем необходимую
    # нам часть данных и сохраняем их в переменную также типом dataframe
    # у нас dataframe, его хэшировать нельзя,
    # поэтому переводим в массив через .values
    X = read_csv.iloc[:, :-1].values
    Y = read_csv.iloc[:, -1].values

    label_encoder = LabelEncoder()
    X[:, 3] = label_encoder.fit_transform(X[:, 3])
    print(X)

