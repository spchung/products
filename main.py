import importlib
from flask import Flask, url_for
from flask_restx import Api

app = Flask(__name__)
class MyApi(Api):
    @property
    def specs_url(self):
        # Monkey patch for HTTPS
        scheme = 'http' if ('8080' in self.base_url or '5000' in self.base_url) else 'https'
        return url_for(self.endpoint('specs'), _external=True, _scheme=scheme)

swaggerApi = MyApi(
    app,
    version='1.0',
    title='Example API',
    description='Whatever you want',
    # security=['apikey', 'account_info', 'preparer_account_info'],
    # authorizations={
    #     'apikey': {
    #         'type': 'apiKey',
    #         'in': 'header',
    #         'name': 'X-API-KEY'
    #     },
    #     'account_info': {
    #         'type': 'apiKey',
    #         'in': 'header',
    #         'name': 'X-API-ACCOUNT',
    #         'description': 'accept both emplid or email'
    #     },
    #     'preparer_account_info': {
    #         'type': 'apiKey',
    #         'in': 'header',
    #         'name': 'X-API-PREPARER',
    #         'description': 'accept both emplid or email'
    #     }
    # }
)

module_mapper = {
    'example': 'example'
}

sorted_moduleMapper = {}
for k, v in sorted(module_mapper.items(), key=lambda x: x[0]):
    sorted_moduleMapper[k] = v


for mod in sorted_moduleMapper:
    tmp = importlib.import_module("api." + mod + '.endpoint')
    swaggerApi.add_namespace(tmp.api, path='/v1/'+module_mapper[mod])

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)