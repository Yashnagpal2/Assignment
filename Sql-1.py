#(1)What is a database? Differentiate between SQL and NoSQL databases.
#Answer SQL Databases
#Structured data with tables
#Fixed schema.
#SQL query language.
#ACID properties.
#Suitable for strict data consistency, structured data, and complex queries.

#NoSQL Databases:

#Variety of data models.
#Dynamic or schema-less.
#Diverse query languages.
#Horizontal scalability.
#Various consistency models.
#Suitable for rapidly changing or unpredictable data."

#(2)What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.

#Answer : DDL stands for "Data Definition Language," and it is a subset of SQL (Structured Query Language) used for defining and managing the structure or schema of a database. DDL commands are used to create, modify, and delete database objects like tables, indexes, and constraints
#Create:
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)
mycursor = mydb.cursor()
mycursor.execute("create table if not exixts test2.table_1(c1 INT , c2 Varchar , c3 Float)")
mydb.close()
#Drop:
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)
mycursor = mydb.cursor()
mycursor.execute("Drop Table Test_1.test2")
mydb.close()
#Alter:
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)
mycursor = mydb.cursor()
mycursor.execute("Alter table if not exixts test2.table_1(add c4 varchar")
mydb.close()

#Truncate:
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)
mycursor = mydb.cursor()
mycursor.execute("Truncate table if not exixts test2.table_1")
mydb.close()

#(3)What is DML? Explain INSERT, UPDATE, and DELETE with an example.
#Answer:DML stands for "Data Manipulation Language," which is a subset of SQL (Structured Query Language). DML commands are used to interact with and manipulate the data stored in a database. The three primary DML commands are INSERT, UPDATE, and DELETE.
#insert:
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)
mycursor = mydb.cursor()
mycursor.execute("Insert into test2.table_1('yash' , 12 ,23)")
mydb.close()

#Delete:
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)
mycursor = mydb.cursor()
mycursor.execute("Delete table test2.table_1")
mydb.close()

#(4)What is DQL? Explain SELECT with an example.
#DQL stands for "Data Query Language," which is a subset of SQL (Structured Query Language). DQL commands are used to retrieve data from a database. The primary DQL command is SELECT, which allows you to query a database table and retrieve specific data based on various conditions.

#Here's an explanation and an example of the SELECT command:
#SELECT: The SELECT command is used to retrieve data from one or more database tables. It allows you to specify which columns to retrieve, filter the rows based on conditions, sort the results, and perform other operations on the data.

#(5)describe primary and foreign key
#Primary Key:

#Uniquely identifies rows in a table.
#Ensures data integrity by requiring uniqueness and non-null values.
#Often indexed for faster data retrieval.
#Used to establish relationships between tables as a reference.
#Foreign Key:

#Establishes relationships between tables by referencing the primary key of another table.
#Enforces data integrity by ensuring data in one table corresponds to data in another.
#Can be optional (nullable) or mandatory (non-nullable).
#Often used to maintain referential integrity and enforce constraints.








