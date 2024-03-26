import psycopg2


def create_table():
    conn = psycopg2.connect(
        database="CMS", user='postgres',
        password='sela0713',
        host='127.0.0.1', port='5432'
    )
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS StudentDetails (
            student_id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            phone_number TEXT NOT NULL,
            aadhar_number TEXT NOT NULL,
            email_id TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
create_table()


def insert_function(name, age, phone_number, aadhar_number, email_id):
    conn = psycopg2.connect(
        database="CMS", user='postgres',
        password='sela0713',
        host='127.0.0.1', port='5432'
    )
    cursor = conn.cursor()
    cursor.execute('''
            INSERT INTO StudentDetails (name, age, phone_number, aadhar_number, email_id)
            VALUES (%s, %s, %s, %s, %s)
        ''', (name, age, phone_number, aadhar_number, email_id))
    conn.commit()
    conn.close()

    return "Student details submitted successfully!"