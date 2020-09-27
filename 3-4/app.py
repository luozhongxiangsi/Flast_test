from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    goods = [{'name': '怪味少女衣服', 'price': 138.00},
             {'name': '怪味少女短裤', 'price': 38.00},
             {'name': '短裤', 'price': 3200.00},
             ]
    return render_template('shop.html', **locals())


if __name__ == '__main__':
    app.run()
