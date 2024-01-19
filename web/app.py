import pymysql
from flask import Flask, jsonify
import os

app = Flask(__name__)

db_host = 'host.docker.internal'
#db_host = os.environ.get('MYSQL_ROOT_HOST')
db_host_password = os.environ.get('MYSQL_ROOT_PASSWORD')
db_user = os.environ.get('MYSQL_USER')
db_password = os.environ.get('MYSQL_PASSWORD')
db_name = os.environ.get('MYSQL_DATABASE')

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/users')
def list_users():
    connection = pymysql.connect(host=db_host,user=db_user, password=db_password, db=db_name)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
