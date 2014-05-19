#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, request, session, g, redirect, url_for, \
             abort, render_template, flash
import RPi.GPIO as GPIO
import time

IO_NO = 23

app = Flask(__name__)

DEBUG = True
SECRET_KEY = 'mktaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' #テキトー

GPIO.cleanup()
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(IO_NO, GPIO.OUT)
GPIO.output(IO_NO, False)

@app.route('/')
def index():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IO_NO, GPIO.OUT)
    GPIO.output(IO_NO, False)
    return render_template('index.jinja')

@app.route('/bloom')
def bloom():
    print "Bloom!"
    return redirect(url_for('bloomed'))

@app.route('/bloomed')
def bloomed():
    try:
        GPIO.output(IO_NO, True)
    except:
        pass

    return render_template('bloomed.jinja')

@app.route('/stop')
def stop():
    GPIO.output(IO_NO, False)
    GPIO.cleanup()
    return redirect('/')

if __name__ == '__main__':
    try:
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(IO_NO, GPIO.OUT)
        GPIO.output(IO_NO, False)
        app.run(host='0.0.0.0')
    except:
        GPIO.cleanup()

