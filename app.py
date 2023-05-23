from flask import Flask, request
from flask_restx import Api, Resource, fields, Namespace
from werkzeug.exceptions import NotFound

app = Flask(__name__)
api = Api(app, version='1.0', title='User API',
    description='A simple User API',
)

ns = Namespace('users', description='User operations')

user_model = ns.model('User', {
    'id': fields.String(required=True, description='The user identifier'),
    'name': fields.String(required=True, description='The user name'),
    'email': fields.String(required=True, description='The user email'),
    'username': fields.String(required=True, description='The user username'),
    'age': fields.Integer(required=True, description='The user age'),
    'occupation': fields.String(required=True, description='The user occupation'),
})


class UserDAO(object):
    def __init__(self):
        self.counter = 0
        self.users = []

    def get(self, id):
        for user in self.users:
            if user['id'] == id:
                return user
        api.abort(404, "User {} doesn't exist".format(id))

    def create(self, data):
        user = data
        user['id'] = self.counter = self.counter + 1
        self.users.append(user)
        return user

    def update(self, id, data):
        user = self.get(id)
        user.update(data)
        return user

    def delete(self, id):
        user = self.get(id)
        self.users.remove(user)

DAO = UserDAO()

@ns.route('/')
class UserList(Resource):
    @ns.doc('create_user')
    @ns.expect(user_model)
    @ns.marshal_with(user_model, code=201)
    def post(self):
        '''Create a new user'''
        return DAO.create(api.payload), 201

    @ns.doc('list_users')
    @ns.marshal_list_with(user_model)
    def get(self):
        '''List all users'''
        return DAO.users

@ns.route('/<string:id>')
@ns.response(404, 'User not found')
@ns.param('id', 'The user identifier')
class User(Resource):
    @ns.doc('get_user')
    @ns.marshal_with(user_model)
    def get(self, id):
        '''Fetch a user given its identifier'''
        return DAO.get(id)

    @ns.doc('delete_user')
    @ns.response(204, 'User deleted')
    def delete(self, id):
        '''Delete a user given its identifier'''
        DAO.delete(id)
        return '', 204

    @ns.expect(user_model)
    @ns.marshal_with(user_model)
    def put(self, id):
        '''Update a user given its identifier'''
        return DAO.update(id, api.payload)

api.add_namespace(ns)

if __name__ == '__main__':
    app.run(debug=True)
