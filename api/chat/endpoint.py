from flask import request
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