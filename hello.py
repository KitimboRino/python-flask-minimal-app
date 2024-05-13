from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    fruits = ['apple', 'banana', 'orange', 'kiwi', 'watermelon', 'mango']
    return render_template('index.html', fruits=fruits)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)