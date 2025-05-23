from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import cv2
import face_recognition
import numpy as np
import base64
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for session management

# Initialize database
def init_db():
    conn = sqlite3.connect('faces.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, encoding BLOB)''')
    conn.commit()
    conn.close()

init_db()

def get_face_encoding(image):
    face_encodings = face_recognition.face_encodings(image)
    return face_encodings[0] if face_encodings else None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('index'))

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data['username']
    image_data = data['image']
    
    image = np.frombuffer(base64.b64decode(image_data), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    face_encoding = get_face_encoding(image)
    
    if face_encoding is not None:
        conn = sqlite3.connect('faces.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, encoding) VALUES (?, ?)", (username, face_encoding.tobytes()))
            conn.commit()
            response = {'status': 'success', 'message': 'User registered successfully'}
        except sqlite3.IntegrityError:
            response = {'status': 'error', 'message': 'Username already exists'}
        conn.close()
    else:
        response = {'status': 'error', 'message': 'No face detected'}
    
    return jsonify(response)

@app.route('/signin', methods=['POST'])
def signin():
    data = request.json
    image_data = data['image']
    
    image = np.frombuffer(base64.b64decode(image_data), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    face_encoding = get_face_encoding(image)
    
    if face_encoding is not None:
        conn = sqlite3.connect('faces.db')
        c = conn.cursor()
        c.execute("SELECT username, encoding FROM users")
        users = c.fetchall()
        conn.close()

        for username, encoding in users:
            stored_encoding = np.frombuffer(encoding, dtype=np.float64)
            matches = face_recognition.compare_faces([stored_encoding], face_encoding)
            if matches[0]:
                session['username'] = username
                return jsonify({'status': 'success', 'message': 'Login successful', 'redirect': url_for('home')})
        return jsonify({'status': 'error', 'message': 'Face not recognized'})
    else:
        return jsonify({'status': 'error', 'message': 'No face detected'})

if __name__ == '__main__':
    app.run(debug=True)
