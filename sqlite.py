import sqlite3

# Connect to SQlite
connection = sqlite3.connect("student.db")


# Create a cursor object to insert the record into the database
cursor = connection.cursor()

# create the table

table_info = """
create table student (NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25) , MARKS INT);
"""
cursor.execute(table_info)

# insert the records
cursor.execute(
    """insert into STUDENT values ('Krish', 'Data Science', 'A' , 90)""")
cursor.execute(
    """insert into STUDENT values ('Sudhanshu', 'Data Science', 'B' , 100)""")
cursor.execute(
    """insert into STUDENT values ('Darius', 'Data Science', 'A' , 86)""")
cursor.execute(
    """insert into STUDENT values ('Vikas', 'DEVOPS', 'A', 50)""")
cursor.execute(
    """insert into STUDENT values ('Dipesh', 'DEVOPS', 'A' , 35)""")

connection.commit()

# Display all records

print("The inserted records are")
data = cursor.execute("""select * from STUDENT""")
for row in data:
    print(row)

connection.close()
