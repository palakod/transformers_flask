import sqlite3
import  json
  
def create_db():
        
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    with open('performOptimize.json') as json_file:  
        data = json.load(json_file)
    json_string = json.dumps(data)

    create_table = 'CREATE TABLE transformers (_id int, user_id int, json_payload text, created_by text, created_on date, modified_by text, modified_on date, output text, notes text )'
    cursor.execute(create_table)

    insert_query = 'INSERT INTO transformers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
        
    transformers = [
        (1442,  442, json_string,'Bhanu', '2019-06-01', 'Quinn', '2019-07-29', 90.5, "notes"),
        (1443,  432, json_string,'John', '2018-12-20', 'Prakash', '2019-02-01', 97.5, "notes"),
        (1444,  467, json_string,'Oliver', '2018-09-21', 'Dan', '2018-11-19', 290.5,  "notes"),
        (1445,  598, json_string,'Ranjeet', '2018-07-22', 'Jones', '2018-08-23', 960.5, "notes")
        ]

    cursor.executemany(insert_query, transformers)

    connection.commit()
    connection.close()

def reg_user():

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    create_table = 'CREATE TABLE users (user_id int, first_name text, last_name text, email_id text, contact_number text)'
    cursor.execute(create_table)

    insert_query = 'INSERT INTO users VALUES (?, ?, ?, ?, ?)'

    users = [
        (442, 'Bhanu', 'Prakash', 'bhanu.prakash@spx.com', '812-098-123'),
        (432, 'Vamshi', 'Krishna', 'vamshi.krishna@spx.com', '814-598-623'),
        (467, 'Ranjeet', 'Kumar', 'ranjeet.kumar@spx.com', '812-058-123'),
        (598, 'Sai', 'Sowmith', 'sai.sowmith@spx.com', '812-038-123')
        ]

    cursor.executemany(insert_query, users)

    connection.commit()
    connection.close()

create_db()
reg_user()
    


