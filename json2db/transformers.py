import sqlite3
from flask_restful import Resource, reqparse
import datetime

header_list = ['_id', 'owner', 'json_payload', 'created_by', 'created_on', 'modified_by', 'modified_on', 'output', 'notes']

class TransformerRegister(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('_id', type = int, required = True, help = "This field cannot be blank.")
    parser.add_argument('owner', type = str, required = True, help = "This field cannot be blank.")
    parser.add_argument('json_payload', type = str, required = True, help = "This field cannot be blank.")
    parser.add_argument('created_by', type = str, required = True, help = "This field cannot be blank.")
    parser.add_argument('created_on', type = str, required = True, help = "This field cannot be blank.")
    parser.add_argument('modified_by', type = str, required = True, help = "This field cannot be blank.")
    parser.add_argument('modified_on', type = str, required = True, help = "This field cannot be blank.")
    parser.add_argument('output', type = str, required = True, help = "This field cannot be blank.")
    parser.add_argument('notes', type = str, required = False)


    def post(self):

        data = TransformerRegister.parser.parse_args()
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO transformers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (data['_id'], data['owner'], data["json_payload"], data['created_by'], data['created_on'], data['modified_by'], data['modified_on'], data['output'], data['notes']))
        connection.commit()
        connection.close()

        return {'message': 'Transformer is sucessfully registered!'}        

class TransformersList(Resource):

    def get(self):
        
        dict_list = []                         
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM transformers'

        for row in cursor.execute(query):           
            result_list = []
            for i in row:
                result_list.append(i)
        
            row_dict = dict(zip(header_list, result_list))
            dict_list.append(row_dict)

            final_output = {'sucess' : True, 'total' : 9, 'page' : 1, 'data' : dict_list}  

        return final_output

class Transformers(Resource):

    def get_by_id(self, _id):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM transformers WHERE _id = ?'

        result = cursor.execute(query, (_id,))
        row_dict = dict(zip(header_list, result))
        final_output = {'sucess' : True, 'total' : 9, 'page' : 1, 'data' : row_dict}

        return final_output



