from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory, g
from flask_sqlalchemy import SQLAlchemy
from flask_api import status
from werkzeug.utils import secure_filename
import os

from graphtec import Graphtec

gt = Graphtec()

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['hpgl', 'plt'])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

db = SQLAlchemy(app)

class FileInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    selected_file = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return "FileInfo('{selected_file}')".format(selected_file = self.selected_file)

selected_file = None
# selected_file = "square_10mm.plt" 


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def main():
    file=FileInfo.query.all()[-1].selected_file
    return render_template('main.html', selected_file=file )

@app.route('/files', methods=['GET', 'POST'])
def upload_file():
        # check if the post request has the file part
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected', 'danger')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
        if not allowed_file(file.filename):
            flash('File type not allowed', 'danger')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('uploaded_file',
            #                         filename=filename))
            # return redirect(url_for('main'))
            flash('File uploaded successfully', 'success')
            return redirect(request.url)
    return render_template('files.html', files = os.listdir('./uploads'), selected_file=selected_file)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/set_active_file/<filename>', methods=['POST'])
def set_active_file(filename):
    db.session.add(FileInfo(selected_file = filename))
    db.session.commit()
    print("setting active file:",)
    return "OKAY", status.HTTP_200_OK

@app.route('/get_active_file')
def get_active_file():
    print("returning active file")
    return FileInfo.query.all()[-1].selected_file, status.HTTP_200_OK

@app.route('/delete_all', methods=['POST'])
def delete_all():
    for file in os.listdir('./uploads'):
        os.remove("./uploads/" + file)
    return redirect(url_for('upload_file'))

@app.route('/run_file/<filename>', methods=['POST'])
def run_file(filename):
    print("Running file:",filename)
    gt.Run(filename)
    return "Running File:", filename, status.HTTP_200_OK

if __name__ == "__main__":
    app.run(debug=True)