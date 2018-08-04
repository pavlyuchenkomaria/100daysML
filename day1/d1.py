import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import Imputer, StandardScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

class Durasha:
    def __init__(self, age=0, name="Masha"):
        # self. это обращение к коробочке с данными (текущему объекту,
        # с которым ты работаешь ---- self. росто показывает,
        #  где хранится переменная)
        self.age = age
        self.name = name

    def get_name(self):
        return self.name

    def sum(self, a, b):
        return a + b

    # self то обязательный аргумент функции  в классе
    def set_age(self, new_age):
        self.age = new_age


if __name__ == '__main__':
# здесь слева название объекта, справа название класса
# в скобочках аргументы
# мы обращаемся к функции инит через объект, который обозначаем как
# названиекласса()
    durasha = Durasha(18, "masha")


    read_csv = pd.read_csv('Data.csv')
    X = read_csv.iloc[:, :-1].values
    Y = read_csv.iloc[:, 3].values
    # создали объект в классе
    imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
    # вызывали ф-ю фит, накормили ее инфой
    imputer = imputer.fit(X[:, 1:3])
    # взяли данные из места, с ними поработали и туда же вернули
    X[:, 1:3] = imputer.transform(X[:, 1:3])

    # создали объект в классе
    label_encoder = LabelEncoder()
    # заменили во всех строках первый столбец
    # с названием страны на цифру для этой страны
    X[ : , 0] = label_encoder.fit_transform(X[ : , 0])

    onehotencoder = OneHotEncoder(categorical_features = [0])
    X = onehotencoder.fit_transform(X).toarray()

    labelencoder_Y = LabelEncoder()
    Y =  labelencoder_Y.fit_transform(Y)

    X_train, X_test, Y_train, Y_test = \
        train_test_split( X , Y , test_size = 0.2, random_state = 0)

    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.fit_transform(X_test)

    print(X_train)

