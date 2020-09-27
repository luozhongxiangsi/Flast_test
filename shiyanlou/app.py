from flask import Flask
from flask_bootstrap import Bootstrap   # 新增代码，引入核心类

from .handlers import blueprint_list


def register_blueprints(app):
    for bp in blueprint_list:
        app.register_blueprint(bp)


def create_app():
    app = Flask(__name__)
    Bootstrap(app)                      # 新增代码，将插件注册到应用中

    register_blueprints(app)

    return app