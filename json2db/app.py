from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api, reqparse

from transformers import TransformerRegister, Transformers_get

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'spx_transformers'
api = Api(app)






api.add_resource(TransformerRegister, '/register')
api.add_resource(Transformers_get, '/v1/objects/<string:owner>')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
