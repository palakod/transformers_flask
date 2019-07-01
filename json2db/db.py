import sqlite3
import  json

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

with open('performOptimize.json') as json_file:  
    data = json.load(json_file)
json_string = json.dumps(data)

create_table = 'CREATE TABLE transformers (_id int, owner text, json_payload text, created_by text, created_on date, modified_by text, modified_on date, output text, notes text )'
cursor.execute(create_table)

insert_query = 'INSERT INTO transformers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
 
transformers = [
    (1442, 'Bhanu', json_string,'Bhanu', '2019-06-01', 'Quinn', '2019-07-29', 90.5, "notes"),
    (1443, 'Vamshi', json_string,'John', '2018-12-20', 'Prakash', '2019-02-01', 97.5, "notes"),
    (1444, 'Jones', json_string,'Oliver', '2018-09-21', 'Dan', '2018-11-19', 290.5,  "notes"),
    (1445, 'Nirav', json_string,'Ranjeet', '2018-07-22', 'Jones', '2018-08-23', 960.5, "notes")
]

cursor.executemany(insert_query, transformers)

connection.commit()
connection.close()

