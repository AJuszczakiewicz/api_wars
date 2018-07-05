import data_handler
from werkzeug import security


def get_planets(page):
    return data_handler.get_planets(page)


def register_user(username, password):
    password = security.generate_password_hash(password)
    registration_data = [username, password]
    try:
        data_handler.add_user_to_db(registration_data)
    except ValueError as err:
        raise ValueError(err)


def login(username, password):
    try:
        hashed_password = data_handler.get_user_password_from_db(username)
    except ValueError:
        return False
    return security.check_password_hash(hashed_password, password)


def verify_session(session):
    try:
        session['logged_in']
    except KeyError:
        session['logged_in'] = False