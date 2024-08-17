from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

host = os.getenv("SERVER")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")

database = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)