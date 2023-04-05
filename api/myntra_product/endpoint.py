from flask import request
from flask_restx import Resource, Namespace, fields
from .controller import *

api = Namespace('MyntraProducts', description='example endpoint')

query_model = api.model('query_model', {
    'product_name': fields.String,
    'product_brand': fields.String,
    'gender': fields.String,
    'description': fields.String,
    'color': fields.String,
    '_offset':fields.Integer,
    '_limit':fields.Integer,
})

@api.route('/<id>')
class Get(Resource):
    def get(self, id):
        return get_product(id), 200

@api.route('/')
class Query(Resource):
    @api.expect(query_model)
    def post(self):
        payload = request.json
        return query_products(payload), 200