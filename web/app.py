# qimport pymysql
import os

import os
import boto3
from flask import Flask, jsonify
from botocore.exceptions import ClientError

app = Flask(__name__)

# db_host = 'host.docker.internal'
# #db_host = os.environ.get('MYSQL_ROOT_HOST')
# db_host_password = os.environ.get('MYSQL_ROOT_PASSWORD')
# db_user = os.environ.get('MYSQL_USER')
# db_password = os.environ.get('MYSQL_PASSWORD')
# db_name = os.environ.get('MYSQL_DATABASE')

dynamodb_region = os.environ.get('AWS_DEFAULT_REGION')
dynamodb_table_name = os.environ.get('DYNAMODB_TABLE_NAME')

dynamodb = boto3.resource('dynamodb', region_name=dynamodb_region)
table = dynamodb.Table(dynamodb_table_name)


@app.route('/')
def hello_world():
    return 'Hello World!'


# @app.route('/users')
# def list_users():
#     connection = pymysql.connect(host=db_host,user=db_user, password=db_password, db=db_name)
#     cursor = connection.cursor(pymysql.cursors.DictCursor)
#     cursor.execute("SELECT * FROM users")
#     users = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return jsonify(users)

@app.route('/users')
def list_users():
    try:
        response = table.scan()
        users = response['Items']
    except ClientError as e:
        print(e.response['Error']['Message'])
        return jsonify({"error": e.response['Error']['Message']}), 500
    return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
