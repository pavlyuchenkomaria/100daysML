import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import Imputer, StandardScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

class Durasha:
    def __init__(self, age=0, name="Masha"):
        # self. это обращение к коробочке с данными (текущему объекту,
        # с которым ты работаешь ---- self. росто показывает,
        #  где хранится переменная) инит это конструктор, создатель объекта
        # и мы вызываем эту функцию, когда создаем новый объект в классе
        self.age = age
        self.name = name

    def get_name(self):
        return self.name

    def sum(self, a, b):
        return a + b

    # self то обязательный аргумент функции  в классе
    def set_name(self, new_name):
        self.name = new_name

    def __str__(self):
        return "Object of Durasha class: name=" \
               + self.name + ", age=" + str(self.age)
# когда мы используем функцию, мы должны понять, будет ли
#  у нее возвращение данных, потому что есть два типа функций:
# те, которые что-то делают и возвращают значение, и те, которые просто
# что-то делают и его нам не возвращают
# когда есть ретерн, мы можем потом написать
# слева *название новой переменной* =
# куда будет сохраняться то, что вернула функция
# если ретерна нет, то будет None
# в функции инит это встроено разработчиками
# для других нужно смотреть в описании к функции

def deniska(a):
    print(a)
    return a**2

if __name__ == '__main__':
# здесь слева название объекта, справа название класса
# в скобочках аргументы
# мы обращаемся к функции инит через объект, который обозначаем как
# названиекласса()
    durasha = Durasha(18, "masha")
    print(durasha.get_name())
    b = deniska(4)
    print(durasha)
    # read_csv = pd.read_csv('Data.csv')
    # X = read_csv.iloc[:, :-1].values
    # Y = read_csv.iloc[:, 3].values
    # # создали объект в классе
    # imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
    # # вызывали ф-ю фит, накормили ее инфой
    # imputer = imputer.fit(X[:, 1:3])
    # # взяли данные из места, с ними поработали и туда же вернули
    # X[:, 1:3] = imputer.transform(X[:, 1:3])
    #
    # # создали объект в классе
    # label_encoder = LabelEncoder()
    # # заменили во всех строках первый столбец
    # # с названием страны на цифру для этой страны
    # X[ : , 0] = label_encoder.fit_transform(X[ : , 0])
    #
    # onehotencoder = OneHotEncoder(categorical_features = [0])
    # X = onehotencoder.fit_transform(X).toarray()
    #
    # labelencoder_Y = LabelEncoder()
    # Y =  labelencoder_Y.fit_transform(Y)
    #
    # X_train, X_test, Y_train, Y_test = \
    #     train_test_split( X , Y , test_size = 0.2, random_state = 0)
    #
    # sc_X = StandardScaler()
    # X_train = sc_X.fit_transform(X_train)
    # X_test = sc_X.fit_transform(X_test)
    #
    # print(X_train)

