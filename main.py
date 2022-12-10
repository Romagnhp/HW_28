
class StackString:

    # закрытая переменная отвечающая за размер стека
    __steckSize = 3

    def __init__(self) -> None:

        # создание пустого списка
        self.__listString = []

    # метод для выталкивание строки из стека 
    # запись через аксессор свойств
    @property
    def listString(self):
        return self.__listString.pop()


    # методо для помещение строки в стек
    # запись через аксессор свойств
    @listString.setter
    def listString(self, newString:str):

        # условие для фиксации р-ра стека
        if len(self.__listString) < self.__steckSize:
            self.__listString.append(newString)
        else:
            print(f'Стек заполнен, max к-во строк - {self.__steckSize}')

    # перегрузка магического метода __len__() для подсчет количества строк в стеке
    def __len__(self):
        return len(self.__listString)
    
    # метод для проверка пустой ли стек
    def emptyStack(self):
        if len(self.__listString) == 0:
            print('Стек пуст')
            return True
        else:
            print('Стек не пустой')
            return False

    # метод для проверки полный ли стек
    def fullSrack(self):
        if len(self.__listString) == self.__steckSize:
            print('Стек полон')
            return True
        else:
            print('Стек не полный')
            return False

    # метод для очистки стека
    def cleanStack(self):
        self.__listString.clear()

    # метод для получение строки (last in) без выталкивания верхней строки из стека
    def getValueStack(self):
        return self.__listString[-1]

    # перегрузка магического метода __str__ для вывода списка стека через print()
    def __str__(self) -> str:
        return f'Стек - {self.__listString}'

steck_1 = StackString()
steck_1.listString = 'roman_1'
steck_1.listString = 'roman_2'
steck_1.listString = 'roman_3'
steck_1.listString = 'roman_4'

# ПРОВЕРКА

# вывод стека
print(steck_1)

# вывод длинны стека в терминал
print(len(steck_1))

# проверка на заполненость 
steck_1.fullSrack()

# улаление елемента стека
print(steck_1.listString)

# вывод стека после изменений
print(steck_1)

# вывод значение елемента (last in)
print(steck_1.getValueStack())

# очистка стека
steck_1.cleanStack()

# проверка на пустой стек
steck_1.emptyStack()