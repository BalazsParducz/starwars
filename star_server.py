from flask import Flask, render_template, request, redirect, url_for, session
import swapi_connector


import DB_queries
import data_manager
from psycopg2 import IntegrityError


app = Flask('starwas')


@app.route('/')
def main():
    planets_data = swapi_connector.all_planets()

    return render_template('star_data.html', planets_data=planets_data)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        new_user = request.form.to_dict()
        new_user['password'] = data_manager.hash_password(new_user['password'])
        try:
            DB_queries.save_registration(new_user)
            return redirect(url_for('main_page'))
        except IntegrityError:
            return render_template('registration.html', message="Username or email is already in use")
    return render_template('registration.html')


@app.route('/logout', methods=['GET'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.path == '/logout':
        session.clear()
        return render_template('index.html')
    if request.method == 'POST' and 'username' not in session:
        username = request.form['username']
        password = request.form['password']
        try:
            user = DB_queries.login(username)[0]
        except IndexError:
            return render_template("index.html", message="Incorrect credentials")
        if 'username' in user:
            if data_manager.verify_password(password, user['password_hash']):
                for key in user:
                    session[key] = user[key]
                return redirect(url_for('main_page'))
    return redirect(url_for('registration'))


def main():
    app.run(
        host="0.0.0.0",
        port=8888,
        debug=True
    )


if __name__ == '__main__':
    main()