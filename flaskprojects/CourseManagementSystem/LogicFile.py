import psycopg2
from flask import *
# import sqlite3
# import os
from Module.StudentModule.StudentLogic import *
from Module.FacultyModule.FacultyLogic import *

app = Flask(__name__)

app.secret_key = '123'

# DATABASE = 'deepak.db'

def create_table():
    conn = psycopg2.connect(
        database="CMS", user='postgres',
        password='sela0713',
        host='127.0.0.1', port='5432'
    )
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            phone_number TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
create_table()

@app.route('/StudentHomepage')
def Student_Homepage():
    # data = StudentHomepage()
    return render_template("Student/StudentHomepage.html")

@app.route('/')
def index():
    return render_template("Project/ProjectHomepage.html")

@app.route('/FacultyHomepage')
def FacultyHomepage():
    # Check if the user is logged in
    if 'user_id' in session:
        return render_template("Faculty/FacultyHomepage.html")
    else:
        return redirect(url_for('loginpagecall'))

@app.route('/signuppagecall')
def signuppagecall():
    return render_template('Project/Signup.html')

@app.route('/signup', methods=['POST'])
def signuplogic():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    phone_number = request.form['phone_number']

    # Insert user into the database
    conn = psycopg2.connect(
        database="CMS", user='postgres',
        password='sela0713',
        host='127.0.0.1', port='5432'
    )
    cursor = conn.cursor()
    cursor.execute('''
            INSERT INTO users (username, password, email, phone_number)
            VALUES (%s, %s, %s, %s)
        ''', (username, password, email, phone_number))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

@app.route('/loginpagecall')
def loginpagecall():
    return render_template('Project/Login.html')

@app.route('/loginlogic', methods=['POST'])
def loginlogic():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = psycopg2.connect(
            database="CMS", user='postgres',
            password='sela0713',
            host='127.0.0.1', port='5432'
        )
        cursor = conn.cursor()

        # Check if the username and password match a record in the database
        cursor.execute('''
                    SELECT * FROM users WHERE username=%s AND password=%s
                ''', (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            # Store the user_id in the session upon successful login
            session['user_id'] = user[0]

            # Redirect based on the length of the username
            if len(username) == 4:
                return redirect(url_for('FacultyHomepage'))
            elif len(username) == 10:
                return redirect(url_for('Student_Homepage'))
            else:
                # Handle other cases or redirect to a default page
                return "<p style='color: red;'>{{ error }}</p>"

        else:
            # Invalid credentials, show an error message
            return render_template('Project/Login.html', error='Invalid username or password')

    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    # Clear the user_id from the session
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/addst')
def student_form():
    return render_template('Faculty/student_Details_form.html')

@app.route('/submit_student', methods=['POST'])
def submit_student():
    name = request.form['name']
    age = request.form['age']
    phone_number = request.form['phone_number']
    aadhar_number = request.form['aadhar_number']
    email_id = request.form['email_id']
    return insert_function(name, age, phone_number, aadhar_number, email_id)
@app.route('/view_students')
def view_students():
    conn = psycopg2.connect(
        database="CMS", user='postgres',
        password='sela0713',
        host='127.0.0.1', port='5432'
    )
    cursor = conn.cursor()
    # Fetch all student records
    cursor.execute('''
        SELECT * FROM StudentDetails
    ''')
    students = cursor.fetchall()

    conn.close()

    return render_template('Faculty/view_students.html', students=students)

@app.route('/crud')
def crud_display():
    return render_template('Faculty/crud.html')


def get_student_by_id(student_id):
    conn = psycopg2.connect(
        database="CMS", user='postgres',
        password='sela0713',
        host='127.0.0.1', port='5432'
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM StudentDetails WHERE student_id = %s', (student_id,))
    student = cursor.fetchone()
    conn.close()
    return student

@app.route('/update')
def student_update():
    return render_template('Faculty/update_student.html')

@app.route('/update_student/<int:student_id>', methods=['GET', 'POST'])
def update_student(student_id):
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        phone_number = request.form['phone_number']
        aadhar_number = request.form['aadhar_number']
        email_id = request.form['email_id']

        conn = psycopg2.connect(
            database="CMS", user='postgres',
            password='sela0713',
            host='127.0.0.1', port='5432'
        )
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE StudentDetails 
            SET name = %s, age = %s, phone_number = %s, aadhar_number = %s, email_id = %s
            WHERE student_id = %s
        ''', (name, age, phone_number, aadhar_number, email_id, student_id))
        conn.commit()
        conn.close()

        return redirect(url_for('home'))

    student = get_student_by_id(student_id)
    if student:
        return render_template('Faculty/view_students.html', student=student)
    else:
        return 'Student not found'


@app.route('/delete_student/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    # student_id = request.form['student_id']
    # Delete student record from the database
    conn = psycopg2.connect(
        database="CMS", user='postgres',
        password='sela0713',
        host='127.0.0.1', port='5432'
    )
    cursor = conn.cursor()
    cursor.execute('DELETE FROM studentdetails WHERE student_id = %s', (student_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('view_students'))


if __name__ == 'main':
    app.run(debug=True)