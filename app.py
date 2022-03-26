from flask import Flask, flash, redirect, render_template, request, url_for

from form import LoginForm

app = Flask(__name__)
# برای حملات
# csrf token
# میباید
#  زیر
app.config['SECRET_KEY'] = 'secretkey'

@app.route("/")
def index():
    name = "ali"
    return render_template("index.html", data=name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if request.form['username'] != 'admin' or request.form['password'] != '12345678':
            flash("invalid")
        else:
            return redirect(url_for('index'))
    return render_template("login.html", title='Login', form=form)

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