import pytest
import flask
from app import app, DAO  # Replace with your actual Flask app module

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def reset_data():
    DAO.users = []
    DAO.counter = 0

def test_create_user(client, reset_data):
    response = client.post('/users/', json={
        'name': 'John',
        'email': 'john@example.com',
        'username': 'johndoe',
        'age': 30,
        'occupation': 'Engineer'
    })
    assert response.status_code == 201
    json_data = flask.json.loads(response.data)
    assert json_data['name'] == 'John'

def test_get_user(client, reset_data):
    # First, create a user to retrieve later
    client.post('/users/', json={
        'name': 'John',
        'email': 'john@example.com',
        'username': 'johndoe',
        'age': 30,
        'occupation': 'Engineer'
    })
    response = client.get('/users/1')
    assert response.status_code == 200
    json_data = flask.json.loads(response.data)
    assert json_data['name'] == 'John'

# def test_update_user(client, reset_data):
#     # First, create a user to update later
#     client.post('/users/', json={
#         'name': 'John',
#         'email': 'john@example.com',
#         'username': 'johndoe',
#         'age': 30,
#         'occupation': 'Engineer'
#     })
#     response = client.put('/users/1', json={
#         'name': 'John Updated',
#         'email': 'johnupdated@example.com',
#         'username': 'johnupdated',
#         'age': 31,
#         'occupation': 'Senior Engineer'
#     })
#     assert response.status_code == 200
#     json_data = flask.json.loads(response.data)
#     assert json_data['name'] == 'John Updated'

# def test_delete_user(client, reset_data):
#     # First, create a user to delete later
#     client.post('/users/', json={
#         'name': 'John',
#         'email': 'john@example.com',
#         'username': 'johndoe',
#         'age': 30,
#         'occupation': 'Engineer'
#     })
#     response = client.delete('/users/1')
#     assert response.status_code == 204

# def test_list_users(client, reset_data):
#     # First, create two users
#     client.post('/users/', json={
#         'name': 'John',
#         'email': 'john@example.com',
#         'username': 'johndoe',
#         'age': 30,
#         'occupation': 'Engineer'
#     })
#     client.post('/users/', json={
#         'name': 'Jane',
#         'email': 'jane@example.com',
#         'username': 'janedoe',
#         'age': 31,
#         'occupation': 'Engineer'
#     })
#     response = client.get('/users/')
#     assert response.status_code == 200
#     json_data = flask.json.loads(response.data)
#     assert len(json_data) == 2
