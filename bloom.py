#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, request, session, g, redirect, url_for, \
             abort, render_template, flash

app = Flask(__name__)

DEBUG = True
SECRET_KEY = 'mktaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' #テキトー

@app.route('/')
def index():
    return render_template('index.jinja')

@app.route('/bloom')
def bloom():
    print "Bloom!"
    return redirect(url_for('bloomed'))

@app.route('/bloomed')
def bloomed():
    return render_template('bloomed.jinja')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

