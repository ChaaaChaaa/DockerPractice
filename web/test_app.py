import pytest
from .app import app
import os
import pymysql
from flask import Flask, jsonify
from dotenv import load_dotenv
load_dotenv()

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello World!'


def test_list_users(client):
    response = client.get('/users')
    print(response.status_code, response.data)  # 상태 코드와 응답 본문 출력
    assert response.status_code == 200



# def test_list_users(client):
#     # 환경 변수 값 확인
#     db_host = os.environ.get('MYSQL_ROOT_HOST')
#     db_password = os.environ.get('MYSQL_ROOT_PASSWORD')
#     db_user = os.environ.get('MYSQL_USER')
#     db_user_password = os.environ.get('MYSQL_PASSWORD')
#     db_name = os.environ.get('MYSQL_DATABASE')
#
#     # 환경 변수 출력 (옵션: 필요에 따라 주석 처리)
#     print("DB Host:", db_host)
#     print("DB Root Password:", db_password)
#     print("DB User:", db_user)
#     print("DB User Password:", db_user_password)
#     print("DB Name:", db_name)
#
#     # 환경 변수 값 검증 (예시)
#     assert db_host is not None
#     assert db_password is not None
#     assert db_user is not None
#     assert db_user_password is not None
#     assert db_name is not None
#
#     # 나머지 테스트 코드 실행
#
#     print(client.get('db_host'))
#
#     response = client.get('/users')
#     assert response.status_code == 200
#     assert isinstance(response.json, list)
#
#     expected_data = [
#         {
#             "email": "chacha@example.com",
#             "id": 1,
#             "username": "chacha"
#         },
#         {
#             "email": "chacha_test@example.com",
#             "id": 2,
#             "username": "chacha_test"
#         }
#     ]
#
#     assert response.json == expected_data

