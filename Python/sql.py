import sqlite3

connection = sqlite3.connect("books.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        title TEXT, 
        pages INTEGER,
        current_page INTEGER,
    )
""")

cursor.execute("""
    DROP TABLE IF EXIST book
    )
""")

cursor.execute("""
    INSERT INTO books VALUES (
        0, 'A great book', 213, 27
    )
""")

cursor.execute("""
    INSERT INTO books VALUES (
        1, 'A great book', 395, 387
    )
""")

rows = cursor.execute("""
   SELECT * FROM books WHERE title ='A great book'
    )
""")

for row in rows: 
    print(row)

cursor.execute("""
    DELETE FROM books WHERE id=0
    )
""")

connection.commit()

connection.close()