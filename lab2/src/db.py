from sqlalchemy import create_engine
from sqlalchemy import text
from dotenv import load_dotenv
import os


load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_USER')


#create_engine => username, password, hostname:port, database
engine = create_engine('postgresql://{}:{}@{}/{}'.format(POSTGRES_USER, POSTGRES_PASSWORD, 'postgres:5432', POSTGRES_DB))

connection = engine.connect()


def search(hash_value):
    query = f"select text_result from ocr.user_requests where hash_value = '{hash_value}'"
    result = connection.execute(text(query)).fetchall()
    if len(result) == 0:
        return False, ""
    return True, result[0][0] 


def add(user_id, hash_value, text_result, created_at):
    command = f"INSERT INTO ocr.user_requests (user_id, hash_value, text_result, created_at) VALUES ({user_id}, '{hash_value}', '{text_result}', timestamp '{created_at}')"
    stmt = connection.execute(text(command))


