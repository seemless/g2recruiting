__author__ = 'matthew smith'

from flask import Flask

UPLOAD_FOLDER = '/tmp/doc_test'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

import g2recruiting.views
