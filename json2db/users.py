import sqlite3
from flask_restful import Resource, reqparse

header_list = ['user_id', 'first_name', 'last_name', 'email_id', 'contact_number']

# Register a User 
class Users(Resource):

    def post(self):

        parser = reqparse.RequestParser()

        parser.add_argument('user_id', type = int, required = True, help = "This field cannot be blank.")
        parser.add_argument('first_name', type = str, required = True, help = "This field cannot be blank.")
        parser.add_argument('last_name', type = str, required = True, help = "This field cannot be blank.")
        parser.add_argument('email_id', type = str, required = True, help = "This field cannot be blank.")
        parser.add_argument('contact_number', type = str, required = True, help = "This field cannot be blank.")

        data = parser.parse_args()
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO users VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, (data['user_id'], data['first_name'], data["last_name"], data['email_id'], data['contact_number'],))
        connection.commit()
        connection.close()

        return {'message': 'User sucessfully registered!'}

    def get(self): # List all the Users from the db.

        dict_list = []                      
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM users'

        for row in cursor.execute(query):           
            result_list = []
            for i in row:
                result_list.append(i)
        
            row_dict = dict(zip(header_list, result_list))
            dict_list.append(row_dict)  

        return dict_list


    def delete(self): 
        
        dict_list = []  
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type = int, required = True, help = "This field cannot be blank.")

        data = parser.parse_args()
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        delete_query = 'DELETE FROM users WHERE user_id =?' #AND owner=?'
        cursor.execute(delete_query, (data['user_id'],))

        query = 'SELECT * FROM users'

        for row in cursor.execute(query):           
            result_list = []
            for i in row:
                result_list.append(i)
        
            row_dict = dict(zip(header_list, result_list))
            dict_list.append(row_dict)  

        return dict_list

# Get the list of Users  by the 'ID number'.
class UsersByID(Resource):

    def get(self, _id):
                                 
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM users WHERE _id=?'
          
        result = cursor.execute(query, (_id,))
        output = result.fetchone()  
        
        return output



