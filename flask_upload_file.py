from flask import Flask
from flask import render_template, request, send_from_directory
import time
import os
from os import path
from werkzeug.utils import secure_filename
import platform
from werkzeug.datastructures import CombinedMultiDict
from form import UploadForm


app = Flask(__name__)

if platform.system() == "Windows":
    slash = '\\'
else:
    platform.system() == "Linux"
    slash = '/'
UPLOAD_PATH = os.path.curdir + slash + 'uploads' + slash


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        if not os.path.exists(UPLOAD_PATH):
            os.makedirs(UPLOAD_PATH)
        form = UploadForm(CombinedMultiDict([request.form, request.files]))
    




