# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

# views.py
from flask import render_template, flash, redirect, url_for
from app import app
from .forms import MyForm

app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = MyForm()
    if form.validate_on_submit():
        flash(f'Submitted {form.name.data}')
        return redirect(url_for('index'))
    return render_template('submit.html', title='Submit', form=form)