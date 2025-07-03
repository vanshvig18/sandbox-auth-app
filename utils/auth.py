import os
import psycopg2
import bcrypt

# Load DB credentials from Streamlit secrets or environment
DB_HOST = os.getenv("DB_HOST", "")
DB_NAME = os.getenv("DB_NAME", "")
DB_USER = os.getenv("DB_USER", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_PORT = os.getenv("DB_PORT", "5432")


def connect_db():
    """Establishes a connection to the PostgreSQL database using environment variables."""
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )


def init_db():
    """Initializes the database by creating the users table if it doesn't exist."""
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


def create_user(username, password):
    """
    Adds a new user to the database with a hashed password.
    Returns True if successful, False otherwise.
    """
    conn = connect_db()
    cur = conn.cursor()
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s);", (username, hashed))
        conn.commit()
        return True
    except Exception as e:
        print("Error creating user:", e)
        return False
    finally:
        cur.close()
        conn.close()


def authenticate_user(username, password):
    """
    Authenticates a user by verifying their password.
    Returns True if credentials are valid, False otherwise.
    """
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE username = %s;", (username,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    if result:
        return bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8'))
    return False
