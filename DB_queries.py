import database_common


@database_common.connection_handler
def register(cursor, register, hash):
    cursor.execute("""
        INSERT INTO users (user_name, user_password)
        VALUES (%(register)s, %(hash)s);
        """, {'hash': hash, 'register': register})

@database_common.connection_handler
def check_user(cursor,login):
    cursor.execute("""
            SELECT user_name FROM users
            WHERE  user_name= %(login)s;
            """, {'login': login})
    data = cursor.fetchall()
    return data

@database_common.connection_handler
def login(cursor,user_name):
    cursor.execute("""
        SELECT user_password FROM users
        WHERE  user_name= %(login)s;
        """,{'login':user_name})
    data=cursor.fetchall()
    return data

@database_common.connection_handler
def get_id_by_user_name(cursor, user_name):
    cursor.execute("""
                    SELECT user_id FROM users
                    WHERE user_name = %(user_name)s;
                   """,
                   {'user_name': user_name})
    received_id = cursor.fetchone()
    return received_id
