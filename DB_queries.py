import database_common


@database_common.connection_handler
def save_registration(cursor, user_data):
    print(user_data)
    cursor.execute("""
                   INSERT INTO users
                   (first_name, last_name, username, password)
                   VALUES  (%(first_name)s, %(last_name)s, %(username)s, %(password)s);
                   """,
                   {"first_name": user_data["first_name"],
                    "last_name": user_data["last_name"],
                    "username": user_data["username"],
                    "password": user_data["password"]
                    }
                   )


@database_common.connection_handler
def check_user(cursor, login):
    cursor.execute("""
                  SELECT username FROM users
                  WHERE  username= %(login)s;
                  """, {'login': login})
    data = cursor.fetchall()
    return data


@database_common.connection_handler
def login(cursor, user_name):
    cursor.execute("""
        SELECT password FROM users
        WHERE  username= %(login)s;
        """,
                   {'login':user_name})
    data=cursor.fetchall()
    return data


@database_common.connection_handler
def get_id_by_user_name(cursor, user_name):
    cursor.execute("""
                    SELECT id FROM users
                    WHERE username = %(user_name)s;
                   """,
                   {'username': user_name})
    received_id = cursor.fetchone()
    return received_id


@database_common.connection_handler
def get_user_id(cursor, id_number):
    cursor.execute(""" 
                    SELECT id FROM users
                    WHERE {0}.id=%(id)s; """.format(table), {"id": id_number})
    return cursor.fetchone()
