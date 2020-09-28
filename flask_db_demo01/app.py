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


db.create_all()


@app.route('/')
def hello_world():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
