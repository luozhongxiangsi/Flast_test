from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
from datetime import datetime


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    publishing_office = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(100), nullable=False)
    storage_time = db.Column(db.DateTime, default=datetime.now())


@app.route('/add')
def add():
    book1 = Book(title='Python基础教程（第三版）', publishing_office='人民邮电出版社', isbn='8899')
    book2 = Book(title='C plus', publishing_office='人民邮电出版社', isbn='9900')
    db.session.add(book1)
    db.session.add(book2)
    db.session.commit()
    return '添加数据成功'


@app.route('/select')
def select():
    result = Book.query.filter(Book.id=='1').first()
    print(result.title)
    return "查询数据成功"


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/update')
def update():
    book3 = Book.query.filter(Book.id=='1').first()
    book3.isbn = 3322
    db.session.commit()
    return "修改成功"


if __name__ == '__main__':
    app.run(debug=True)
