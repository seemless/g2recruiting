__author__ = 'root'

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
        file_name = form.resume
        print(file_name)
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
