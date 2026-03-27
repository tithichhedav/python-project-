from db_connection import connect_db

conn = connect_db()
print("Connected successfully!")

cursor = conn.cursor()
cursor.execute("SELECT * FROM rooms")

for row in cursor:
    print(row)

conn.close()