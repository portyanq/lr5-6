import templates

# Реализовать два класса: User, Connection.
# Внутри в методах реализовать CRUD (основные методы по работе с данными: select, update, insert)

# класс - структура/сущность со структурой, которую реализует какой-то конкретный объект
# например пользователь Elena или Irina




class User():

    def __init__(self, name, height):
        self.__name = name
        self.__height = height

        if not all([name, height]):
            raise Exception('enter name and height')     

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        print('setter')
        if name != None:
            if (len(name) < 3):
                raise ValueError('lenght name to small')
        
        self.__name = name

        if name == None:
            del self.name # Почему тут не приватная переменная??????????????????????????

    @name.deleter
    def name(self):
        print('deleter')

    @property
    def height(self):
        print('height')
        return self.__height

    def __check_height(self, height):
        pass

    def __check_name(self, name):
        pass

    def select(self, conn, sqlquery):
        sqlquery = "SELECT (?,?) FROM user WHERE (???)"


u1 = User('Nick', 1.85)
print(u1.name, u1.height)

u1.name = 'Nikolai'
print(u1.name)
u1.name = None
print(u1.name)

print('-----')

u1 = User('Elena', 1.69)
u3 = User('Irina', 1.80)

# u1.name = 'el'
print(u1.name)

# u1.name = "Anna"

def singleton(cls):
    import functools

    instance = None
    
    @functools.wraps(cls)
    def inner(*args, **kwargs):
        nonlocal instance
        print(args, kwargs)
        if instance is None:
            instance = cls(*args, **kwargs) # == Connection(dbfile, dbtype='sqlite')
        return instance

    return inner

@singleton
class Connection():
    """

    """
    def __init__(self, dbfile, dbtype='sqlite'):
        self.__filename = dbfile
        self.__conn = None
        self.__cursor = None
        # проверка наличия файла с БД и выбрасываем исключение, если файла нет или он пустой

    def connect(self):
        import sqlite3
        self.__conn = sqlite3.connect(self.__filename)
        self.__cursor = self.__conn.cursor()
        return self.__conn

    @property
    def conn(self):
        return self.__conn

    @property
    def cursor(self):
        return self.__cursor


c = Connection('zhukov.db')
c.connect() # 
c.conn # используем getter
c1 = Connection('zhukov123.db')

print(id(c1), id(c))

print(type(c))

# # Insert a row of data
# sql = "INSERT INTO user(name, height) VALUES(?, ?)"
# names = [('Elena', 1.69), ('Irina', 1.80)]

# conn.executemany(sql, names)

# # Save (commit) the changes
# # conn.commit()

# # READ aka SELECT
crud_read_str = "SELECT * FROM user"
# "SELECT * FROM user WHERE name='Konstantin'"
curs = c.cursor
crud_res = curs.execute(crud_read_str)

for r in crud_res:
    print(r)

# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# conn.close()



if __name__ == '__main__':
    pass

 