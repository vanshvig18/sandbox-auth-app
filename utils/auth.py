import psycopg2
from psycopg2 import sql

def connect_db():
    return psycopg2.connect(
        dbname="sandbox_db",
        user="postgres",
        password="your_password",
        host="localhost",
        port="5432"
    )

def init_db():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def create_user(username, password):
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except:
        return False

def authenticate_user(username, password):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result is not None
