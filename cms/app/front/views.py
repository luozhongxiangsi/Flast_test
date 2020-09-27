# encoding:utf-8
from flask import Blueprint

bp = Blueprint("front", __name__)


@bp.route('/')
def index():
    return "这是前面首页"
