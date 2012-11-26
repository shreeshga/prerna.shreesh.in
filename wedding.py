#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['BOOTSTRAP_USE_CDN'] = True


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html',error='404')


if __name__ == '__main__':
    app.run(debug=True)
