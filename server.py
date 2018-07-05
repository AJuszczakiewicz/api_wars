from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
import logic


app = Flask(__name__)
app.secret_key = 'superSecretCodecoolPassword'
bootstrap = Bootstrap(app)


@app.route('/')
def index(page=1):
    logic.verify_session(session)
    planets = logic.get_planets(page)
    return render_template('index.html', planets=planets, page=page)


@app.route('/<page>')
def next_pages(page=1):
    logic.verify_session(session)
    planets = logic.get_planets(page)
    return render_template('index.html', planets=planets, page=page)


@app.route('/registration', methods=['GET', 'POST'])
def register():
    logic.verify_session(session)
    if session['logged_in']:
        return redirect(url_for('main_page'))
    if request.method == "GET":
        return render_template('signup.html')
    if request.method == "POST":
        login = request.form['username']
        password = request.form['pwd']
        try:
            logic.register_user(login, password)
        except ValueError as err:
            flash("Username taken.")
            return render_template('signup.html')
        return redirect('/')


@app.route('/login', methods=['GET', 'POST'])
def login():
    logic.verify_session(session)
    if session['logged_in']:
        return redirect(url_for('index'))
    if request.method == "GET":
        return render_template('login.html')
    if request.method == "POST":
        login = request.form['username']
        password = request.form['pwd']
        validation = logic.login(login, password)
        if validation:
            session['logged_in'] = True
            session['username'] = login
            flash('Logged in succesfully')
            return redirect(url_for('index'))
        flash("Wrong login credentials provided.")
        return render_template('login.html')


@app.route("/logout")
def logout():
    logic.verify_session(session)
    session.clear()
    session['logged_in'] = False
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)