import os
from flask import Flask,request, render_template,session,redirect,url_for
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
from gtts import gTTS
import pyodbc
from googletrans import Translator
from threading import Timer
app = Flask(__name__)
app.secret_key = 'secret_key'
connection = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-5G09K3A\SQLEXPRESS;'
    'Database=users;'
    'Trusted_connection=yes;')
    #'uid=username;'
    #'pwd=password;'


ALLOWED_EXTENSIONS = {'pdf'}
app.config['MAX_CONTENT_LENGTH'] = 50 * 1000 * 1000
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def clean_folder(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
def schedule_folder_clean():
    Timer(120, schedule_folder_clean).start() # schedule the next cleaning in 2 minutes
    clean_folder("./static/audios/")
schedule_folder_clean()
@app.route('/')
def home():
    return render_template("log_in.html")
@app.route('/log_in',methods=['GET', 'POST'])
def log_in():
    # if request.method == 'POST':
        # Check username and password
        # If valid, redirect to dashboard
        # If invalid, show error message
     #   return render_template('index.html')
    # else:  
     #   return render_template('log_in.html')
     if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", username)
        user = cursor.fetchone()
        if user and user[2] == password:
            session['user_id'] = user[0]
            return render_template('index.html')
        else:
            error_m = 'Invalid username or password'
            return render_template('log_in.html', error_m=error_m)
     else:
        return render_template('log_in.html')
@app.route('/sign_up',methods=['GET', 'POST'])
def sign_up(): 
  #  if request.method == 'POST':
        # Create new user in database
        # Redirect to login page
   #     return redirect(url_for('log_in'))
    #else:
     #   return render_template("sign_up.html")
     if request.method == 'POST':
        email =request.form['email']
        username = request.form['username']
        password = request.form['password']
       # confirm_password = request.form['confirm_password']
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", username)
        user = cursor.fetchone()
        if user:
            error_m = 'Username already taken'
            return render_template('sign_up.html',error_m=error_m)
      #  elif password != confirm_password:
       #     error = 'Passwords do not match'
        #    return render_template('signup.html', error=error)
        else:
            cursor.execute("INSERT INTO users (email,username, password) VALUES (?,?, ?)", email,username, password)
            connection.commit()
            return redirect(url_for('log_in'))
     else:
        return render_template('sign_up.html')
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))
@app.route('/convert',methods=['GET', 'POST'])
def convert():
    if request.method == 'POST':
        if 'pdf' not in request.files:
            error_msg="No file chosen. Please upload a file"
            return render_template("index.html",error_msg=error_msg)
        file = request.files['pdf']
        if file.filename == '':
            error_msg="No file chosen. Please upload a file"
            return render_template("index.html",error_msg=error_msg)
        if file and allowed_file(file.filename):
               sfilename = secure_filename(file.filename)
               file_path = os.path.join('static/uploads', file.filename)
               file.save(file_path)
            # Extract text from the PDF
               text = ''
               with open(file_path, 'rb') as pdf_file:
                    pdf_reader = PdfReader(pdf_file)
                    for page in range(pdf_reader.getNumPages()):
                        page_text = pdf_reader.getPage(page).extractText()
                        text += page_text
    # Translate text to the selected language
               selected_language= request.form["chosen_voice"]
               translator = Translator()
               translated_text = translator.translate(text, dest=selected_language).text
    # Convert translated text to speech
               tts = gTTS(text=translated_text, lang=selected_language)
               audio_path = os.path.join('static/uploads/', 'audio.mp3')
               tts.save(audio_path)
        else:
            error_msg="Only pdf files are allowed"
            return render_template("index.html",error_msg=error_msg)
    return render_template("audio.html",audio_file=audio_path)
if __name__ == '__main__':
    app.run(debug=True)