__author__ = 'root'

import os
from g2recruiting import app
from flask import request, redirect, render_template, url_for
from werkzeug.utils import secure_filename

import forms

@app.route('/test')
def test():
    return 'hi'


@app.route('/login')
def login():
    return 'please login'

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegistrationForm(request.form)

    if request.method == 'POST' and form.validate():
        print (form)
        uploaded_file = request.files['resume']
        ext = uploaded_file.filename.split('.')[-1]
        if uploaded_file and ext in form.allowed_extensions:
            file_name = secure_filename(uploaded_file.filename)
            loc = uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
            print loc
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
