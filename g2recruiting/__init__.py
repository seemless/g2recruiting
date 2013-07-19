__author__ = 'matthew smith'

from flask import Flask
from flask.ext.bootstrap import Bootstrap

UPLOAD_FOLDER = '/tmp/doc_test'
app = Flask(__name__)
Bootstrap(app)
app.config['BOOTSTRAP_USE_CDN'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


import g2recruiting.views
