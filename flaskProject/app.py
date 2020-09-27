from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    titile = "python的键值对"
    author = "tom_jack"
    return render_template('index.html', var1=titile, var2=author)


@app.route('/user/<username>')
def user(username):
    return render_template('user.html', name=username)


if __name__ == '__main__':
    app.run()
