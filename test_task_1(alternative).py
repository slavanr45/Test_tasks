import time


class TreeStore:
    """обработка массива объектов"""

    def __init__(self, data: list):
        """Конструктор для инициализации атрибутов"""
        self.items = data

    def getAll(self) -> list:
        """Возвращает изначальный массив элементов"""
        return self.items

    def getItem(self, n: int) -> dict:
        """Принимает id элемента и возвращает сам объект элемента"""
        for elem in self.items:
            if elem['id'] == n:
                return elem
        print('Введен некорректный id элемента')

    def getChildren(self, n: int) -> list:
        """Принимает id элемента и возвращает массив элементов, являющихся дочерними для того элемента"""
        return [elem for elem in self.items if elem['parent'] == n]

    def getAllParents(self, n: int) -> list:
        """Принимает id элемента и возвращает массив из цепочки родительских элементов"""
        res, tmp_parent = [], None
        for elem in sorted(self.items, key=lambda x: -x['id']):
            if tmp_parent == elem['id']:
                res.append(elem)
                tmp_parent = elem['parent']
            if n == elem['id']:
                tmp_parent = elem['parent']
        return res


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]
ts = TreeStore(items)
start = time.perf_counter()  # вычисление быстродействия методов

print(ts.getAll())  # items
print(ts.getItem(7))  # {"id":7,"parent":4,"type":None}
print(ts.getChildren(4))  # [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
print(ts.getChildren(5))  # []
print(ts.getAllParents(7))  # [{"id":4,"parent":2,"type":"."},{"id":2,"parent":1,"type":"."},{"id":1,"parent":"root"}]

print(time.perf_counter() - start)  # вычисление быстродействия методов
