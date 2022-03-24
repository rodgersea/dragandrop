import zipfile

from flask import Flask, render_template, request, redirect, url_for, send_file, safe_join
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from zipfile import ZipFile, ZipInfo
import sys
import os
from io import BytesIO
from glob import glob

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    print('_________________________________________________________________________', file=sys.stderr)
    print('upload_file()\n', file=sys.stderr)

    if request.method == 'POST':
        upload_files = request.files.getlist('file')
        zip_buffer = BytesIO()
        zipfolder = ZipFile(zip_buffer, 'w', compression=zipfile.ZIP_STORED)

        for file in upload_files:
            try:
                print('_________________________________', file=sys.stderr)
                print('file: ', file.filename, '\n', str(type(file)), file=sys.stderr)
            except:
                pass
            file.save(secure_filename(file.filename))
            zipfolder.write(file.filename)
        zipfolder.close()
        zip_buffer.seek(0)

        return send_file(zip_buffer, mimetype='zip', attachment_filename='test.zip', as_attachment=True)
        # os.remove('test.zip')


if __name__ == '__main__':
    app.run(debug=False, threaded=True)
