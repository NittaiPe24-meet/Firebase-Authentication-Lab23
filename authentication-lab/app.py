from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

config = {
  "apiKey": "AIzaSyDRGjO3hLbaGuUzNjjoUxEuw16Xwadkr7I",
  "authDomain": "yello-ed04e.firebaseapp.com",
  "projectId": "yello-ed04e",
  "storageBucket": "yello-ed04e.appspot.com",
  "messagingSenderId": "29543276179",
  "appId": "1:29543276179:web:10a8c74944ae275127f766",
  "measurementId": "G-QZ9QW2LPND",
  "databaseURL": "https://yello-ed04e-default-rtdb.firebaseio.com"
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
           return redirect(url_for('add_tweet'))
        except:
           error = "Authentication failed"
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():methods
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)