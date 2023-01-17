import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

default_db_name = os.getenv("DATABASE_NAME")


def init_connection(db_name: str):
    if db_name == '':
        db_name = default_db_name
    db_host = os.getenv("DATABASE_HOST")
    cnxn_str = (
        'Driver={ODBC Driver 17 for SQL Server};' +
        'Server=' + str(db_host) + ';' +
        'Database=' + db_name + ';' +
        'UID=' + str(os.getenv("DATABASE_USERNAME")) + ';' +
        'PWD=' + str(os.getenv("DATABASE_PASSWORD")) + ';' +
        'Encrypt=YES;TrustServerCertificate=YES'
    )
    print(cnxn_str)
    try:
        connection = pyodbc.connect(cnxn_str)
        return connection.cursor()
    except Exception as e:
        print('Fail to connect DB')
        print(e)
    