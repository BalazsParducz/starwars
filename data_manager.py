import datetime
import bcrypt
import database_common
import DB_queries
from flask import session


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


def hash_password(plain_text_password):
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def login_check():
    if 'username' in session:
        login_value = 'username'
    else:
        login_value = False
    return login_value


def permission_check(table, id_number):
    user_id = DB_queries.get_user_id(id_number)['users_id']
    if session['id'] == user_id:
        permission = True
    else:
        permission = False
    return permission



