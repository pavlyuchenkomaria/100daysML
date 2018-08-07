import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

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
    one_hot_encoder = OneHotEncoder(categorical_features=[3])
    X = one_hot_encoder.fit_transform(X).toarray()

    X = X[:, 1:]

    X_train, X_test, Y_train, Y_test =\
        train_test_split(X, Y, test_size=0.2, random_state=0)

    linear_regression = LinearRegression()
    linear_regression = linear_regression.fit(X_train, Y_train)

    Y_pred = linear_regression.predict(X_test)

    print(Y_test)
    print(Y_test - Y_pred)
