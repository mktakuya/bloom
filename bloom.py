#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, request, session, g, redirect, url_for, \
             abort, render_template, flash
import RPi.GPIO as GPIO
import time

# で始まる行はコメント行。

IO_NO = 23 # 使うピン番号の設定。今回はGPIO23番ピン。
# 参考： http://openrtm.org/openrtm/sites/default/files/5274/raspberrypi_gpio_pinassign.png

app = Flask(__name__)

DEBUG = True
SECRET_KEY = 'mktaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' #テキトー

GPIO.cleanup() # GPIO初期化

GPIO.setmode(GPIO.BCM) # GPIOピン番号を用いる
GPIO.setup(IO_NO, GPIO.OUT) # GPIOのIO_NO番をOUTモードに
GPIO.output(IO_NO, False) # GPIOのIO_NO番をFalseに

@app.route('/')
def index(): # http://hogehoge:5000/ にアクセスされたら実行する
    GPIO.cleanup() # GPIOを初期化
    GPIO.setmode(GPIO.BCM) # GPIOピン番号を用いる
    GPIO.setup(IO_NO, GPIO.OUT) # GPIOのIO_NO番をOUTモードに
    GPIO.output(IO_NO, False) # GPIOのIO_NO番をFalseに
    return render_template('index.jinja') # indexページを表示

@app.route('/bloom')
def bloom(): # http://hogehoge:5000/ にある Bloomボタンが押された時の処理
    try:
        GPIO.output(IO_NO, True) # GPIOのIO_NO番をTrueに（3.3V出力）
        print "Bloom!"
    except:
        pass

    return redirect(url_for('bloomed')) # http://hogehoge:5000/bloomed へリダイレクト

@app.route('/bloomed')
def bloomed(): # http://hogehoge:5000/bloomed にアクセスされたら実行する
    return render_template('bloomed.jinja')

@app.route('/stop')
def stop(): # http://hogehoge:5000/bloomed にあるStopボタンが押された時の処理
    GPIO.output(IO_NO, False)
    GPIO.cleanup()
    return redirect('/')

if __name__ == '__main__': # ここから下はいじらないで
    try:
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(IO_NO, GPIO.OUT)
        GPIO.output(IO_NO, False)
        app.run(host='0.0.0.0')
    except:
        GPIO.cleanup()

