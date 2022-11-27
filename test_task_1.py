class TreeStore:
    """
    Обработка массива объектов по заданному условию с помощью дерева.
    Для выполнения требования максимального быстродействия и прямого доступа к элементам без поиска,
    представим дерево, как объединенный список родителей и список потомков)

    логическое представление дерева исходных данных следующее:
    вершины дерева:     0 1 2 3 4 5 6 7 8
    ссылка на родителя:   r 1 1 2 2 2 4 4
    ссылки на потомков:   2 4   7
                          3 5   8
                            6

    программно дерево представляет список кортежей:
    [(), ('root', [2, 3], []), (1, [4, 5, 6], 'test'), (1, [], 'test'), (2, [7, 8], 'test'),
           (2, [], 'test'), (2, [], 'test'), (4, [], None), (4, [], None)]
    где нулевой элемент не используется, для упрощения восприятия кода ревьювером,
    т.е. id элемента будет равняться порядковому номеру вершины в списке

    ! в задании требуется максимальное быстродействие и не обговорена возможность ввода
    заведомо некорректных данных, поэтому исключена проверка id элемента на IndexError

    ! в задании не уточнено могут ли id идти не последовательно и начинаться не с единицы.
    Поэтому конструктор построен несколько усложненным, учитывающим любую точку начала
    и последовательность id.
    """

    def __init__(self, data: list):
        """Конструктор"""
        self.items = data  # сохраняем исходный массив для метода getAll

        tmp_d, maximum = {}, 0
        for elem in data:  # отдельный цикл для потомков, этим исключаем n^2 обходов в осн цикле
            tmp_d.setdefault(elem['parent'], []).append(elem['id'])
            maximum = max(maximum, elem['id'])

        self.tree = [tuple() for _ in range(maximum + 1)]
        for elem in data:  # основной цикл формирования дерева
            tmp_childs = tmp_d[elem['id']] if elem['id'] in tmp_d else []
            tmp_type = elem['type'] if elem['id'] != 1 else []
            self.tree[elem['id']] = (elem['parent'], tmp_childs, tmp_type)

    def getAll(self) -> list:
        """Возвращает изначальный массив элементов.
        В задании требуется максимальное быстродействие, и отсутствуют требования к ресурсам,
        поэтому быстрее всего сохранить и вернуть исходный массив без обработки"""
        return self.items

    def getItem(self, n: int) -> dict:
        """Принимает id элемента и возвращает сам объект элемента. Прямой доступ к элементу"""
        if n == 1:
            return {'id': n, 'parent': self.tree[n][0]}
        return {'id': n, 'parent': self.tree[n][0], 'type': self.tree[n][2]}

    def getChildren(self, n: int) -> list:
        """Принимает id элемента и возвращает массив элементов, являющихся дочерними"""
        res = []
        for elem in self.tree[n][1]:
            res.append(self.getItem(int(elem)))
        return res

    def getAllParents(self, n: int) -> list:
        """Принимает id элемента и возвращает массив из цепочки родительских элементов"""
        res = []
        tmp_parent = self.tree[n][0]
        while tmp_parent != 'root':
            res.append(self.getItem(tmp_parent))
            tmp_parent = self.tree[tmp_parent][0]
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

print(ts.getAll())  # items
print(ts.getItem(7))  # {"id":7,"parent":4,"type":None}
print(ts.getChildren(4))  # [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
print(ts.getChildren(5))  # []
print(ts.getAllParents(7))  # [{"id":4,"parent":2,"type":"."},{"id":2,"parent":1,"type":"."},{"id":1,"parent":"root"}]
