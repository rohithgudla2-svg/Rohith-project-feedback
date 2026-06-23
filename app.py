from flask import Flask, render_template, request, redirect, session
import sqlite3
import os
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
db_path=os.path.join(BASE_DIR,"feedback.db")

app = Flask(__name__)
app.secret_key = "feedback_secret_key"


# ---------------- HOME / LOGIN ----------------
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def check():

    student_id = request.form['student_id']
    password = request.form['password']

    conn = sqlite3.connect(db_path, check_same_thread=False)

    c = conn.cursor()

    c.execute(
        "SELECT * FROM students WHERE student_id=? AND password=?",
        (student_id, password)
    )

    user = c.fetchone()
    conn.close()

    if user:
        session['student_id'] = user[0]
        session['name'] = user[1]
        return redirect('/dashboard')

    return "Invalid Login"


# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():

    if 'student_id' not in session:
        return redirect('/')

    return render_template('dashboard.html', name=session['name'])


# ---------------- GIVE FEEDBACK ----------------
@app.route('/give-feedback')
def give_feedback():

    if 'student_id' not in session:
        return redirect('/')

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("SELECT student_id, name FROM students")
    students = c.fetchall()

    conn.close()

    return render_template('give_feedback.html', students=students)


@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():

    if 'student_id' not in session:
        return redirect('/')

    giver_id = session['student_id']
    receiver_id = request.form['receiver_id']
    rating = request.form['rating']
    comment = request.form['comment']

    if giver_id == receiver_id:
        return "You cannot give feedback to yourself."

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute(
        "SELECT * FROM feedback WHERE giver_id=? AND receiver_id=?",
        (giver_id, receiver_id)
    )

    if c.fetchone():
        conn.close()
        return "Already submitted feedback."

    c.execute("""
        INSERT INTO feedback (giver_id, receiver_id, rating, comment)
        VALUES (?, ?, ?, ?)
    """, (giver_id, receiver_id, rating, comment))

    conn.commit()
    conn.close()

    return redirect('/dashboard')


# ---------------- MY FEEDBACK ----------------
@app.route('/my-feedback')
def my_feedback():

    if 'student_id' not in session:
        return redirect('/')

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("""
        SELECT rating, comment
        FROM feedback
        WHERE receiver_id=?
    """, (session['student_id'],))

    feedbacks = c.fetchall()
    conn.close()

    return render_template('my_feedback.html', feedbacks=feedbacks)


# ---------------- CHANGE PASSWORD ----------------
@app.route('/change-password', methods=['GET', 'POST'])
def change_password():

    if 'student_id' not in session:
        return redirect('/')

    if request.method == 'POST':

        old_password = request.form['old_password']
        new_password = request.form['new_password']

        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute("""
            SELECT * FROM students
            WHERE student_id=? AND password=?
        """, (session['student_id'], old_password))

        user = c.fetchone()

        if not user:
            conn.close()
            return "Old password is incorrect"

        c.execute("""
            UPDATE students
            SET password=?
            WHERE student_id=?
        """, (new_password, session['student_id']))

        conn.commit()
        conn.close()

        return redirect('/dashboard')

    return render_template('change_password.html')


# ---------------- ADMIN LOGIN ----------------
@app.route('/admin-login')
def admin_login():
    return render_template('admin_login.html')


@app.route('/admin-check', methods=['POST'])
def admin_check():

    username = request.form['username']
    password = request.form['password']

    if username == "rohith" and password == "rohith9550":
        session['admin'] = True
        return redirect('/admin')

    return "Invalid Admin Login"


# ---------------- ADMIN DASHBOARD ----------------
@app.route('/admin')
def admin():

    if 'admin' not in session:
        return redirect('/admin-login')

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("""
        SELECT receiver_id,
               COUNT(*) as total_feedback,
               ROUND(AVG(rating),2) as avg_rating
        FROM feedback
        GROUP BY receiver_id
    """)

    results = c.fetchall()
    conn.close()

    return render_template('admin.html', results=results)


# ---------------- ADMIN VIEW DETAILS ----------------
@app.route('/admin-view/<student_id>')
def admin_view(student_id):

    if 'admin' not in session:
        return redirect('/admin-login')

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("""
        SELECT giver_id, rating, comment
        FROM feedback
        WHERE receiver_id=?
    """, (student_id,))

    data = c.fetchall()
    conn.close()

    return render_template('admin_view.html', data=data, student_id=student_id)


# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/admin-logout')
def admin_logout():
    session.pop('admin', None)
    return redirect('/admin-login')


# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True)