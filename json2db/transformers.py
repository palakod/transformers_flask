import sqlite3
from flask_restful import Resource, reqparse
import datetime

header_list = ['_id', 'owner', 'json_payload', 'created_by', 'created_on', 'modified_by', 'modified_on', 'output', 'notes']

# Register a Transformer
class Transformers(Resource):

    def post(self):

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
        data = parser.parse_args()
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO transformers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (data['_id'], data['owner'], data["json_payload"], data['created_by'], data['created_on'], data['modified_by'], data['modified_on'], data['output'], data['notes']))
        connection.commit()
        connection.close()

        return {'message': 'Transformer is sucessfully registered!'}

    def get(self): # List all the Transformers from the db.
        
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
    
    def put(self): # Change the owner of the transformer(project).

        parser = reqparse.RequestParser()

        parser.add_argument('_id', type = int, required = True, help = "This field cannot be blank.")
        parser.add_argument('owner', type = str, required = True, help = "This field cannot be blank.")

        data = parser.parse_args()
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        update = 'UPDATE transformers SET owner=? WHERE _id=?'
        cursor.execute(update, (data['owner'], data['_id']))
        connection.commit()

        query = 'SELECT * FROM transformers WHERE _id=?'
        result = cursor.execute(query, (data['_id'],))
        output = result.fetchone()                            #fetchone()	This method returns one record as a tuple, If there are no more records then it returns None
        row = dict(zip(header_list, output))
        
        final_output = {'sucess' : True, 'total' : 1, 'page' : 1, 'data' : row}  

        return final_output

    def delete(self):

        dict_list = [] 

        parser = reqparse.RequestParser()

        parser.add_argument('_id', type = int, required = True, help = "This field cannot be blank.")
        # parser.add_argument('owner', type = str, required = True, help = "This field cannot be blank.")

        data = parser.parse_args()
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        delete_query = 'DELETE FROM transformers WHERE _id =?' #AND owner=?'
        cursor.execute(delete_query, (data['_id'],))

        query = 'SELECT * FROM transformers'

        for row in cursor.execute(query):           
            result_list = []
            for i in row:
                result_list.append(i)
        
            row_dict = dict(zip(header_list, result_list))
            dict_list.append(row_dict)

            final_output = {'sucess' : True, 'total' : len(dict_list), 'page' : 1, 'data' : dict_list}  

        return final_output


# Get the list of Transformers owned by 'owner'.
class TransformersByOwner(Resource):

    def get(self, owner):
        
        dict_list = []                         
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM transformers WHERE owner=?'

        for row in cursor.execute(query, (owner,)):           # Since there can be a same owner for multiple transformers we use for loop to query.
            result_list = []
            for i in row:
                result_list.append(i)
        
            row_dict = dict(zip(header_list, result_list))
            dict_list.append(row_dict)

            final_output = {'sucess' : True, 'total' : len(dict_list), 'page' : 1, 'data' : dict_list}  

        return final_output

# Get the list of Transformers by the 'ID number'.
class TransformersByID(Resource):

    def get(self, _id):
                                 
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM transformers WHERE _id=?'      # Since the id of transformer is unique, we don't need a for loop.
          
        result = cursor.execute(query, (_id,))
        output = result.fetchone()
        row = dict(zip(header_list, output))

        final_output = {'sucess' : True, 'total' : 1, 'page' : 1, 'data' : row}  

        return final_output



