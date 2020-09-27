from flask import Flask
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='lz1003!!', db='demo_01', charset='utf8')
cursor = conn.cursor()
sql = "select * from user"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    username = row[0]
    email = row[1]
    print(username)
    print(email)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
