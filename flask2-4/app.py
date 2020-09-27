from flask import Flask
from flask import url_for, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("首先访问了index()这个视图函数了！")
    url1 = url_for('user_login')
    return redirect('/user_login')


@app.route('/user_login')
def user_login():
    return "这是用户登录页面，请你登录，才能访问首页！"


if __name__ == '__main__':
    app.run()
