from flask import request
from flask_restx import Resource, Namespace, fields
from .controller import *

api = Namespace('Example', description='example endpoint')

example_model = api.model('example_model', {
    'id': fields.String,
    'message': fields.String
})

parser = api.parser()
parser.add_argument('message', type=str, help='Message to echo', location='args')

@api.route('/<id>')
class Example1(Resource):
    def get(self, id):
        return get_message(id)

@api.route('/echo')
class Example2(Resource):
    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        return args['message'], 200

@api.route('/health')
class Example3(Resource):
    def get(self):
        return "ok", 200

@api.route('/')
class Example4(Resource):
    @api.expect(example_model)
    def post(self):
        payload = self.api.payload
        return save_message(payload)