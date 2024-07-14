# "Режимы открытия файлов"
import os


class Product:
    """
    Product('Potato', 50.0, 'Vagetables')
    Атрибут name - название продукта (строка).
    Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
    Атрибут category - категория товара (строка).
    Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'
    """

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    """
    Метод get_products(self), считывает всю информацию из файла __file_name,
    Метод add(self, *products), добавляет в файл __file_name каждый продукт из products,
    """
    __file_name = 'products.txt'

    def __init__(self):
        if not os.path.exists(self.__file_name):  # файл не существует
            file = open(self.__file_name, "w")
            file.close()

    def get_products(self):
        file = open(self.__file_name, "r")
        file_string = file.read()
        file.close()
        return file_string

    def add(self, *products):
        for product in products:
            file_string = self.get_products()
            file = open(self.__file_name, "a")
            if product.name in file_string:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(str(product) + '\n')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

# Вывод на консоль:
# Первый запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Второй запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato уже есть в магазине
# Продукт Spaghetti уже есть в магазине
# Продукт Potato уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
