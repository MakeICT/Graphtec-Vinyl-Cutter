from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
from flask_api import status
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['hpgl', 'plt'])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

selected_file = None
# selected_file = "square_10mm.plt" 


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def main():
    return render_template('main.html')

@app.route('/files', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file selected')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if not allowed_file(file.filename):
            flash('File type not allowed')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('uploaded_file',
            #                         filename=filename))
            # return redirect(url_for('main'))
            return redirect(request.url)
    return render_template('files.html', files = os.listdir('./uploads'), selected_file=selected_file)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/set_active_file/<filename>', methods=['POST', 'GET'])
def set_active_file(filename):
    selected_file = filename
    print("setting active file")
    return "OKAY", status.HTTP_200_OK

@app.route('/delete_all', methods=['POST'])
def delete_all():
    for file in os.listdir('./uploads'):
        os.remove("./uploads/" + file)
    return redirect(url_for('upload_file'))

if __name__ == "__main__":
    app.run(debug=True)