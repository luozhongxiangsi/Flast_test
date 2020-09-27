# encoding:utf-8
from flask import Flask
from app.admin import bp as admin_bp
from app.common import bp as commont_bp
from app.front import bp as front_bp

app = Flask(__name__)
app.register_blueprint(admin_bp)
app.register_blueprint(commont_bp)
app.register_blueprint(front_bp)
app.config.from_object('config')


@app.route('/')
def hello_world():
    return "hello world!"


if __name__ == '__main__':
    app.run(debug=True)