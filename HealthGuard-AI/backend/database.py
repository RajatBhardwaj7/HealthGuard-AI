import sqlite3

DATABASE_NAME = "../database/healthguard.db"


def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    # -----------------------------
    # Users Table
    # -----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            email TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    # -----------------------------
    # Prediction History Table
    # -----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prediction_history(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_email TEXT NOT NULL,

            pregnancies INTEGER,

            glucose REAL,

            blood_pressure REAL,

            skin_thickness REAL,

            insulin REAL,

            bmi REAL,

            diabetes_pedigree_function REAL,

            age INTEGER,

            prediction TEXT,

            probability REAL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    conn.commit()
    conn.close()


# =====================================
# USER FUNCTIONS
# =====================================

def user_exists(email):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


def create_user(name, email, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users(name,email,password)
        VALUES(?,?,?)
        """,
        (name, email, password)
    )

    conn.commit()
    conn.close()


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


# =====================================
# PREDICTION HISTORY FUNCTIONS
# =====================================

def save_prediction(
    user_email,
    pregnancies,
    glucose,
    blood_pressure,
    skin_thickness,
    insulin,
    bmi,
    dpf,
    age,
    prediction,
    probability
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO prediction_history(

            user_email,
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            diabetes_pedigree_function,
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
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            dpf,
            age,
            prediction,
            probability
        )
    )

    conn.commit()
    conn.close()


def get_prediction_history(user_email):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM prediction_history
        WHERE user_email=?
        ORDER BY created_at DESC
        """,
        (user_email,)
    )

    history = cursor.fetchall()

    conn.close()

    return history