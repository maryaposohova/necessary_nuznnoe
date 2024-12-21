class Point:
    MAX_CORD = 100
    MIN_CORD = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if Point.MIN_CORD <= x <= self.MAX_CORD:
            self.x = x
            self.y = y

# переопределяем аттрибут в методе, в классе он остается прежним
    def set_bount(self, left):
        self.MIN_CORD = left

# можем изменить аттрибут в классе
    @classmethod
    def set_bount(cls, left):
        cls.MIN_CORD = left

# возвр значеие аттрибута
    def __getattribute__(self, item):
        print('__getattribute__')
        return  object.__getattribute__(self, item)

 # запретить доступ к аттрибуту
    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('доступ запрещен')
        else:
            return  object.__getattribute__(self, item)

# запретить создавать аттрибут
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('Oшибка аттрибута')
        else:
            # object.__setattr__(self, key, value)
            # self.x = value    # будет выполняться по рекурсии
            self.__dict__[key] = value

# если нет элемента, чтобы вышел фолс а не ошибка
    def __getattr__(self, item):
        # print('__getattr__ ' + item)
        return False

# вызывается при удалении аттрибута
    def __delattr__(self, item):
        # print('__delattr__: ' + item)
        object.__delattr__(self, item)

pt1 = Point(3,2)
pt2 = Point(7,2)
pt1.d = 6
pt1.z = 5
print(pt1.yy)
del pt1.x
print(pt1.__dict__)