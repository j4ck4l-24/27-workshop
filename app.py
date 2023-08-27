from flask import Flask, render_template, request, redirect, make_response, session
import sqlite3
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def process_login():
    username = request.form.get('username')
    password = request.form.get('password')

    conn = sqlite3.connect('userdb.db')
    cursor = conn.cursor()
    conn.create_function("sleep", 1, time.sleep)

    cursor.execute("SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'")
    result = cursor.fetchall()

    conn.close()

    if result:
        session['logged_in'] = True
        return redirect('/dashboard')
    else:
        return "Invalid credentials."

@app.route('/dashboard')
def welcome():
    if not session.get('logged_in'):
        return redirect('/')  
    return render_template('flag.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4020, debug=False)

