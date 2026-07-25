import sqlite3
import os


# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Create database folder path
DATABASE_DIR = os.path.join(BASE_DIR, "database")

os.makedirs(DATABASE_DIR, exist_ok=True)


DATABASE_NAME = os.path.join(
    DATABASE_DIR,
    "healthguard.db"
)



def get_connection():

    conn = sqlite3.connect(
        DATABASE_NAME
    )

    conn.row_factory = sqlite3.Row

    return conn



def create_tables():

    conn = get_connection()

    cursor = conn.cursor()


    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)


    # Predictions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_email TEXT NOT NULL,
        pregnancies INTEGER,
        glucose INTEGER,
        bloodpressure INTEGER,
        skinthickness INTEGER,
        insulin INTEGER,
        bmi REAL,
        diabetespedigreefunction REAL,
        age INTEGER,
        prediction TEXT,
        probability REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)


    conn.commit()
    conn.close()



def create_user(name, email, password):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users(name,email,password)
        VALUES(?,?,?)
        """,
        (name,email,password)
    )

    conn.commit()
    conn.close()



def user_exists(email):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    return user is not None



def login_user(email):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    return user



def save_prediction(
    user_email,
    pregnancies,
    glucose,
    bloodpressure,
    skinthickness,
    insulin,
    bmi,
    diabetespedigreefunction,
    age,
    prediction,
    probability
):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO predictions(
        user_email,
        pregnancies,
        glucose,
        bloodpressure,
        skinthickness,
        insulin,
        bmi,
        diabetespedigreefunction,
        age,
        prediction,
        probability
        )
        VALUES(?,?,?,?,?,?,?,?,?,?,?)
        """,
        (
            user_email,
            pregnancies,
            glucose,
            bloodpressure,
            skinthickness,
            insulin,
            bmi,
            diabetespedigreefunction,
            age,
            prediction,
            probability
        )
    )


    conn.commit()
    conn.close()



def get_prediction_history(email):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT *
        FROM predictions
        WHERE user_email=?
        ORDER BY created_at DESC
        """,
        (email,)
    )


    history = cursor.fetchall()

    conn.close()


    return history