from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
import sys

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(secure_filename(uploaded_file.filename))
        return 'file uploaded successfully'


if __name__ == '__main__':
    app.run(debug=True)
