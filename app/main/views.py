from . import main
from flask import render_template


@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')


@main.route('/entry')
def entry():
    return render_template('entry.html')


@main.route('/about')
def about():
    return render_template('about.html')
