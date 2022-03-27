from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from itsdangerous import json
from form import LoginForm
from flask_sqlalchemy import SQLAlchemy
# from keystoneclient.session import Session
# from flask_script import Manager
# from flask_migrate import Migrate
#, MigrateCommand
app = Flask(__name__)
# برای حملات
# csrf token
# میباید
#  زیر
app.config['SECRET_KEY'] = 'secretkey'
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# migrate = Migrate(app, db)
#manager = Manage(app)
#manager.add_command('db', MigrateCommand)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    email = db.Column(db.String(100), unique = True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

@app.route("/")
def index():
    # for row in session.query(User, User.username).all():
    #     print(row.User, row.username)
    # users = session.query(User).order_by(User.id)
    # return jsonify(str(users))
    users = User(username = "amontazeri", email = "ahmad")
    session.add_all(users)
    session.commit()

    # name = "ali"
    # return render_template("index.html", data=users)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()

#     if form.validate_on_submit():
#         if request.form['username'] != 'admin' or request.form['password'] != '12345678':
#             flash("invalid")
#         else:
#             return redirect(url_for('index'))
#     return render_template("login.html", title='Login', form=form)

# @app.errorhandler(404)
# def page_not_found():
#     return render_template('404.html')

# @app.errorhandler(403)
# def page_not_found():
#     return render_template('403.html')

# @app.errorhandler(500)
# def page_not_found():
#     return render_template('500.html')  

if __name__ == '__main__':
    app.run(debug=True)