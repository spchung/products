from flask import request, make_response
from flask_restx import Resource, Namespace, fields
from .controller import *



api = Namespace('Chat', description='open ai chat endpoint')

chat_model = api.model('chat_model', {
    'query': fields.String,
})

@api.route('/')
class Chat(Resource):
    @api.expect(chat_model)
    def post(self):
        user_input = request.json['query']
        return chat(user_input), 200
    
    def options(self):
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
        return response