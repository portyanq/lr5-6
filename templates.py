def connect_to_db(path_to_db: str) -> object:
    """
    Connect to sqlite database
    
    :return sqlite3.Connection
    """
    import sqlite3
    import os.path
    
    if os.path.isfile('./'+ path_to_db):
        return sqlite3.connect(path_to_db)
    else:
        raise FileNotFoundError()


def create_table(conn, table_name, domens_lst):
    
    if conn:
        cur = conn.cursor()
        cur.execute(f"create table if not exists {table_name} {domens_lst}")
        conn.commit()
        # conn.close()
    else:
        raise TypeError(' connetction error ')



def insert_param_data(conn, table_name, values):

    if conn:
        cur = conn.cursor()
        cur.execute(f"INSERT INTO {table_name} VALUES {values}")
        conn.commit()
        # conn.close()
    else:
        raise TypeError(' connetction error ')


def read_data (conn, table_name, domen, operator, value):

    if conn:
        cur = conn.cursor()
        iterat = cur.execute(f"SELECT * from {table_name} WHERE {domen}{operator}{value}")
        for i in iterat:
            print(i)

        conn.commit()
        # conn.close()
    else:
        raise TypeError(' connetction error ')


def update_data(conn, table_name, update_param, update_value, domen_u, operator_u, value_u):
    
    if conn:
        cur = conn.cursor()
        cur.execute(f"SELECT * from {table_name}")
        data = cur.fetchone()

        if data is not None:
            upd = cur.execute(f"UPDATE {table_name} SET {update_param} = {update_value} \
                WHERE {domen_u}{operator_u}{value_u}")
        else:
            raise NameError('no data')

        conn.commit()
        # conn.close()
    else:
        raise TypeError(' connetction error ')


def delete_data(conn, table_name, domen, value):

    if conn:
        cur = conn.cursor()
        conn.execute(f"DELETE from {table_name} where {domen} = {value};")

        conn.commit()
        # conn.close()
    else:
        raise TypeError(' connetction error ')


def connetction_close(conn):
    
    if conn:
        conn.close()
    else:
        raise TypeError(' connetction error ')




if __name__ == '__main__':
    table_name='user'
    #create
    domens_lst = '(id, height, name, delected, created_at)'

    #insert
    values = (6, 1.75, 'test', 0, '2019-03-02 11:39:20')
    
    #read
    domen = 'height'
    operator = '<'
    value = 1.8

    # update
    domen_u = 'height'
    operator_u = '='
    value_u = 'Null'
    update_param = 'height'
    update_value = 1.5

    #delete
    domen_d = 'id'
    value_d = 6

    conn = templates.connect_to_db('zhukov.db')
    templates.create_table(table_name, domens_lst, conn)
    templates.insert_param_data(conn, table_name, values=str(values))
    templates.read_data(conn, table_name, domen=domen, operator=operator, value=value)
    templates.update_data(conn, table_name, update_param=update_param, update_value=update_value, domen_u=domen_u, operator_u=operator_u, value_u=value_u)
    templates.delete_data(conn, table_name, domen=domen_d, value=value_d)
    templates.connetction_close(conn)



