from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql.cursors
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')
PORT = os.getenv('APP_PORT', 5000)

def get_db_connection():    
    return pymysql.connect(
        host=os.getenv('MYSQL_HOST', ''),
        user=os.getenv('MYSQL_USER', ''),
        password=os.getenv('MYSQL_PASSWORD', ''),
        db=os.getenv('MYSQL_DB', ''),
        cursorclass=pymysql.cursors.DictCursor
    )

# Create table if not exists
conn = get_db_connection()
with conn.cursor() as cursor:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            completed BOOLEAN DEFAULT FALSE
        )
    """)
conn.commit()
conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT id, title, completed FROM todos")
        todos = cursor.fetchall()
    conn.close()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form['title']
    if not title:
        flash('Title is required!', 'danger')
        return redirect(url_for('index'))
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO todos (title) VALUES (%s)", (title,))
    conn.commit()
    conn.close()
    flash('Todo added!', 'success')
    return redirect(url_for('index'))

@app.route('/complete/<int:todo_id>')
def complete_todo(todo_id):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("UPDATE todos SET completed=TRUE WHERE id=%s", (todo_id,))
    conn.commit()
    conn.close()
    flash('Todo marked as completed!', 'info')
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM todos WHERE id=%s", (todo_id,))
    conn.commit()
    conn.close()
    flash('Todo deleted!', 'warning')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=PORT)
