import sqlite3
from flask_restful import Resource, reqparse
import datetime

class Transformers_get(Resource):
    def __init__(self, id, owner, json_payload, created_by, created_on, modified_by, modified_on, output, notes):
        self.id = id
        self.owner = owner
        self.json_payload = json_payload
        self.created_by = created_by
        self.created_on = created_on
        self.modified_by = modified_by
        self.modified_on = modified_on
        self.output = output
        self.notes = notes
    
    @classmethod
    def find_by_id(cls, id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM transformers WHERE id=?"
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        if row:
            transformer = cls(*row)
        else:
            transformer = None

        connection.close()
        return transformer

    @classmethod
    def find_by_owner(cls, owner):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM transformers WHERE owner=?"
        result = cursor.execute(query, (owner,))
        row = result.fetchone()
        if row:
            transformer = cls(*row)
        else:
            transformer = None

        connection.close()
        return transformer

class TransformerRegister(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('id', type = int, required = True, help = "This field cannot be blank.")
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
        cursor.execute(query, (data['id'], data['owner'], data["json_payload"], data['created_by'], data['created_on'], data['modified_by'], data['modified_on'], data['output'], data['notes']))

        connection.commit()
        connection.close()

        return {'message': 'Transformer is sucessfully registered!'}