import os


class BaseConfig:
    '''
    基础配置类， 存储公共配置项
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'asdfasdf'
    SQLALCHEMY_