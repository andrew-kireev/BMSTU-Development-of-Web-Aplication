# Порождающий шаблон Singleton


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DbConnection:
    def select(self, request):
        print('Произведен такой запрос к базе данных:' + request)
        print('Получены какие-то данные...')

    def insert(self, request):
        print('Произведен такой запрос к базе данных:' + request)
        print('В BD вставлены такие-то данные...')


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = DbConnection()
            print('Соединение BD установленно')
        else:
            print('Соединение с BD уже установленно')

    def select(self, request):
        if self.connection is not None:
            self.connection.select(request)
        else:
            print('Соединение с базой данных отсутствует')

    def insert(self, request):
        if self.connection is not None:
            self.connection.insert(request)
        else:
            print('Соединение с базой данных отсутствует')


if __name__ == '__main__':
    db_singleton_1 = Database()
    print(db_singleton_1)
    db_singleton_2 = Database()
    print(db_singleton_2)

    db_singleton_1.insert('INSERT INTO table1 2')
    db_singleton_2.connect()
    db_singleton_1.insert('INSERT INTO table1 2')
