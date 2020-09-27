from flask import Flask, url_for


app = Flask(__name__)


@app.route("/")
def index():
    url1 = (url_for('news', id='10086'))
    return "URL反转内容为：%s" % url1


@app.route('/news/<id>')
def news(id):
    return u'你的请求参数是：%s' %id


if __name__ == '__main__':
    app.run(debug=True)