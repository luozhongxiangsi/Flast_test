from flask import Flask
from flask import render_template
import random

app = Flask(__name__)


@app.route('/')
def hello_world():
    rand1 = random.randint(0, 1)
    return render_template('index.html', name=rand1)


if __name__ == '__main__':
    app.run(debug=True)
