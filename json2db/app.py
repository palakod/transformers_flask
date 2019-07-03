from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api, reqparse
from transformers import Transformers, TransformersByOwnerID, TransformersByID
from users import Users, UsersByID

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'spx_transformers'
api = Api(app)

api.add_resource(Transformers, '/transformer') # POST, GET, PUT and DELETE.
api.add_resource(TransformersByOwnerID, '/owner/<int:user_id>')
api.add_resource(TransformersByID, '/id/<int:_id>')

api.add_resource(Users, '/user') # POST, GET and DELETE
api.add_resource(UsersByID, '/id/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True