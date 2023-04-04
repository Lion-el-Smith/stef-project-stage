import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE cars (license_plate string, hrs_parked int, car_color string, is_dirty boolean, price float,PRIMARY KEY (license_plate))"
cursor.execute(create_table)

car1 = ('ad2568', 4, 'red', True, 28)
insert_query = "INSERT INTO cars VALUES (?,?,?,?,?)"
cursor.execute(insert_query, car1)

cars1 = [
    ('ad1568', 6, 'red', True, 42),
    ('ad6568', 7, 'blue', True, 49),
    ('ad3568', 4, 'green', False, 28),
    ('ad4568', 8, 'silver', True, 56),
    ('ad5568', 6, 'brown', False, 42),
]
cursor.executemany(insert_query, cars1)

select_query = "SELECT * FROM cars"

for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()
