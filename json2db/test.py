import sqlite3



def put(_id, owner, new_owner):

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    query = 'UPDATE transformers SET owner=? WHERE _id=? AND owner=?'
    result = cursor.execute(query, (new_owner ,_id, owner))
    print(result)
    connection.commit()
    connection.close()

def get(_id):
         
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM transformers WHERE _id=?'
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        header_list = ['_id', 'owner', 'json_payload', 'created_by', 'created_on', 'modified_by', 'modified_on', 'output', 'notes']
        dict_row = dict(zip(header_list, row))
        print(dict_row)
        print()
        print()

get(1442)