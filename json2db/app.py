from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api, reqparse

from transformers import Transformers, TransformersByOwner, TransformersByID, ChangeOwner

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'spx_transformers'
api = Api(app)

api.add_resource(Transformers, '/transformer')
api.add_resource(TransformersByOwner, '/owner/<string:owner>')
api.add_resource(TransformersByID, '/id/<int:_id>')
api.add_resource(ChangeOwner, '/change_owner/<int:_id>/<string:owner>/<string:new_owner>')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True