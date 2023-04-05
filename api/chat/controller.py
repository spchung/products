import os
import openai
from api.myntra_product.controller import query_products

def chat(user_input):
    completion = GPT_3().query_products(user_input)
    try:
        completion = completion['choices'][0]['text']
        # process completion
        entities = completion.strip().split(';')
        d = {}
        for entitiy in entities:
            if ':' not in entitiy:
                continue
            key, value = entitiy.split(':')
            d[key] = value
        return query_products(d)
    except Exception as e:
        raise(e)

class GPT_3:
    def __init__(self):
        self.api_key = os.getenv("OPEN_AI_KEY")
        openai.api_key = self.api_key
        self.completion = openai.Completion
        self.options = {
            'engine': 'text-davinci-003',
            'temperature': 0,
            'top_p': 1,
            'frequency_penalty': 0,
            'presence_penalty': 0,
            'max_tokens': 100,
            'stop': ['\n'],
        }

    def __complete(self, prompt, options=None):
        if not options:
            options = self.options

        return self.completion.create(prompt=prompt, **options)

    def query_products(self, user_input):
        prompt = f'''
        Extract entities from prompt
        prompt: red dress
        entities: product_name:dress;product_brand:;gender:women;price:;color:red;description:;
        prompt: grey puma backpack with backzip
        entities: product_name:dress;product_brand:puma;gender:women;price:;color:Grey;description:backzip;
        prompt: {user_input}
        entities:
        '''
        return self.__complete(prompt)