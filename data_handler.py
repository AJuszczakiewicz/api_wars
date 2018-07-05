from config import config
import requests
import psycopg2
import psycopg2.extras


def open_database():
    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)
        connection.autocommit = True

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return connection


def connection_handler(funct):
    def wrapper(*args, **kwargs):
        connection = open_database()
        # we set the cursor_factory parameter to return with a RealDictCursor cursor (cursor which provide dictionaries)
        dict_cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        ret_value = funct(dict_cursor, *args, **kwargs)
        dict_cursor.close()
        connection.close()
        return ret_value

    return wrapper


def get_planets(page_number):
    if page_number == 1:
        return requests.get("https://swapi.co/api/planets").json()
    else:
        return requests.get("https://swapi.co/api/planets/?page={0}".format(page_number)).json()


@connection_handler
def add_user_to_db(cursor, registration_data):
    query = """SELECT * FROM users WHERE username=%s;"""
    username = [registration_data[0]]
    cursor.execute(query, username)
    if cursor.fetchall():
        raise ValueError("Username taken.")
    query = """INSERT INTO users (username, password) VALUES (%s, %s);"""
    cursor.execute(query, registration_data)


@connection_handler
def get_user_password_from_db(cursor, username):
    username = [username]
    query = """SELECT password FROM users WHERE username = %s;"""
    cursor.execute(query, username)
    try:
        password = cursor.fetchall()[0]['password']
    except IndexError:
        raise ValueError("User not found")
    return password
