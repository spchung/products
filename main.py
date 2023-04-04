import importlib, os
from flask import Flask, url_for, send_from_directory
from flask_restx import Api
from flask_cors import CORS
from shared.connection import db

app = Flask(__name__)
class MyApi(Api):
    @property
    def specs_url(self):
        # Monkey patch for HTTPS
        scheme = 'http' if ('8080' in self.base_url or '5000' in self.base_url) else 'https'
        return url_for(self.endpoint('specs'), _external=True, _scheme=scheme)

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTGRES_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

swaggerApi = MyApi(
    app,
    version='1.0',
    title='Example API',
    description='Whatever you want',
)

module_mapper = {
    'example': 'example',
    'myntra_product':'myntra_product'
}

sorted_moduleMapper = {}
for k, v in sorted(module_mapper.items(), key=lambda x: x[0]):
    sorted_moduleMapper[k] = v


for mod in sorted_moduleMapper:
    tmp = importlib.import_module("api." + mod + '.endpoint')
    swaggerApi.add_namespace(tmp.api, path='/v1/'+module_mapper[mod])

db.init_app(app)
CORS(app)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=False)