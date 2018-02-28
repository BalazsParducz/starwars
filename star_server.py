from flask import Flask, render_template, request, redirect, url_for, session
import swapi_connector
import json
import DB_queries
import data_manager
from psycopg2 import IntegrityError
counter=0

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def main_page():
    url_dict = {}
    global counter
    if request.args.get("direction"):
        if request.args.get("direction") == "next":
            counter+=1
            if counter==7:
                counter=6

        elif request.args.get("direction") == "prev":
            if counter==0:
                counter=0
            else:
                counter-=1
    planets_data = swapi_connector.all_planets(counter)
    for item in planets_data:
        item["nr_of_residents"] = item["residents"]
    url_dict["residents"] = planets_data[0]["residents"]
    url_dict = json.dumps(planets_data, ensure_ascii=False)
    logged_user = data_manager.login_check()
    return render_template("star_data.html",
                           planets_data=planets_data,
                           residents=url_dict,
                           logged_user=logged_user
                           )


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
        return render_template("star_data.html")
    if request.method == 'POST':   #and 'username' not in session
        username = request.form['username']
        password = request.form['password']
        try:
            user = DB_queries.login(username)[0]
            session["username"] = username
        except IndexError:
            return render_template('star_data.html', message="Incorrect credentials")
        if 'username' in user:
            if data_manager.verify_password(password, user['password_hash']):
                for key in user:
                    session[key] = user[key]
                return redirect(url_for('main_page'))
    return redirect(url_for('main_page'))





def main():
    app.run(
        host="0.0.0.0",
        port=8888,
        debug=True
    )


if __name__ == '__main__':
    main()