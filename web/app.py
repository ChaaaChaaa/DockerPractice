import pymysql
from flask import Flask, jsonify

app = Flask(__name__)


def get_db_connection():
    return pymysql.connect(host='host.docker.internal',
                           user='docker_chacha',
                           password='1q2w3e4r',
                           db='dockerdb',
                           charset='utf8mb4')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/users')
def list_users():
    connection = get_db_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
