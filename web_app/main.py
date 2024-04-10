from flask import Flask, render_template, request
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

# Функция для установления соединения с базой данных
def connect_to_database():
    conn = psycopg2.connect(
        host='localhost',
        dbname='mydatabase',
        user='user1',
        password='test'
    )
    return conn
@app.route('/view', methods=['POST'])
def view():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view.html', users=users)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (username, email, password)
            VALUES (%s, %s, %s)
        ''', (username, email, password))
        conn.commit()
        cursor.close()
        conn.close()
        return 'Запись успешно добавлена в базу данных'


if __name__ == '__main__':
    app.run(debug=True)