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
        zf = ZipFile('test.zip', 'w')
        memory_file = BytesIO()
        with ZipFile(memory_file, 'w') as zf:
            upload_files = request.files.getlist('file')
            for file in upload_files:
                try:
                    print('_________________________________', file=sys.stderr)
                    print('file: ', file.filename, '\n', str(type(file)), file=sys.stderr)
                except:
                    pass
                if file != '':
                    file.save(secure_filename(str(file)))
                    data = ZipInfo(file.filename)
                    data.compress_type = zipfile.ZIP_DEFLATED
                    zf.writestr(data, file.filename)
        memory_file.seek(0)

        return send_file(memory_file, attachment_filename='test.zip', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
