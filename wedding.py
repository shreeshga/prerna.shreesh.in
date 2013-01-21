#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

TIMELINEJS_FOLDER = 'lib/TimelineJS/compiled/js/'
NORMAL_GALLERY_FOLDER = 'static/wedding_gallery/normal'
THUMB_GALLERY_FOLDER = 'static/wedding_gallery/thumb'

app = Flask(__name__)
Bootstrap(app)
app.config['BOOTSTRAP_USE_CDN'] = True
app.config['TIMELINEJS_FOLDER'] = TIMELINEJS_FOLDER


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/wedding')
def wedding():
    return render_template('wedding.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/gallery')
def gallery():
    normal = [os.path.join(NORMAL_GALLERY_FOLDER,x) for x in os.listdir(NORMAL_GALLERY_FOLDER)]
    thumb = [os.path.join(THUMB_GALLERY_FOLDER,x) for x in os.listdir(THUMB_GALLERY_FOLDER)]
    return render_template('gallery.html',normal= normal,thumb=thumb,zip =zip)

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html',error='404')


if __name__ == '__main__':
    app.run(debug=True)
