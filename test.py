import sqlite3

connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()

def add_to_database(attribute_name, holland_id):
    sql = "INSERT INTO main_attribute (id, attribute_name, holland_code_id) VALUES (?, ?, ?)"
    cursor.execute(sql, (None, attribute_name, holland_id))
    connection.commit()

with open("tools.txt", 'r') as file:
    content = file.readlines()

for line in content:
    add_to_database(line, 1)
    print(line)
print("Success")
