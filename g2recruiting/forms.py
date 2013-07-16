__author__ = 'matthew smith'

from wtforms import Form, BooleanField, TextField, FileField, \
                    validators
from flask.ext.uploads import UploadSet, DOCUMENTS

docs = UploadSet('resumes',DOCUMENTS)

class RegistrationForm(Form):
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    resume = FileField("Upload your image",
        validators=[])
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])

    allowed_extensions = ['doc','docx','pdf','txt','rtf','odf','ods']