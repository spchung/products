from flask import request
from flask_restx import Resource, Namespace, fields
from .controller import *

api = Namespace('Example', description='example endpoint')

example_model = api.model('example_model', {
    'id': fields.String,
    'message': fields.String
})

@api.route('/<id>')
class Example(Resource):
    def get(self, id):
        return get_message(id), 200

@api.route('/')
class Example2(Resource):
    @api.expect(example_model)
    def post(self):
        payload = self.api.payload
        return save_message(payload), 200 