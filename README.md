# Face Recognition Login

## Description
This project is a web-based face recognition login system built with Flask. It allows users to sign up by registering their face encoding along with a username, and then sign in using face recognition via their webcam. The system uses OpenCV and the `face_recognition` library to capture and process face images, and stores user data in a SQLite database.

## Features
- User sign-up with face image and username
- User sign-in using face recognition
- Session management to keep users logged in
- Simple and intuitive web interface with webcam integration

## Technologies Used
- Python
- Flask
- OpenCV
- face_recognition
- SQLite
- HTML, CSS, JavaScript

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/charanhajari/face_recognition_login_system
   cd face_recognition_login
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required Python packages:
   ```
   pip install flask opencv-python face_recognition numpy
   ```

4. **Note:** If you encounter issues related to installing face recognition models, try running the following command in your terminal:
   ```
   pip install setuptools
   ```

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Use the webcam interface to:
   - Sign Up: Enter a username and capture your face image to register.
   - Sign In: Capture your face image to log in.

4. Upon successful login, you will be redirected to a welcome page.

## File Structure

- `app.py` - Main Flask application with routes and face recognition logic.
- `faces.db` - SQLite database storing user face encodings.
- `templates/` - HTML templates for the web pages (`index.html` for login/signup, `home.html` for welcome page).
- `static/` - Static assets such as images (e.g., background image `abc.png`).

## Notes
- Ensure your webcam is enabled and accessible by the browser.
- The face recognition accuracy depends on the quality of the webcam and lighting conditions.
- The secret key in `app.py` should be changed for production use.

## License
This project is open source and available under the MIT License.
