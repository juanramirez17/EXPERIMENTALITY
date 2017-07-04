# -*- coding: utf-8 -*-

# flask + mqtt + mysql + plot (highcharts.js)
# Author :  Juan Pablo Ramirez G
# Date : July 4, 2017

import json
from time import time
from random import random
from flask import Flask, render_template, make_response, request
from flaskext.mysql import MySQL
import paho.mqtt.client as mqtt
import datetime

# initialization of mysql from flask
mysql = MySQL()
port = 5000
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'test_DB'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)
temperature = 0;

# Recieve Messagge and save to database
def on_message(client, userdata, msg):
    global temperature
    print "MQTT Data Received..."
    print(msg.topic+" "+str(msg.payload))
    print "MQTT Topic: " + msg.topic
    print "Data: " + msg.payload
    conn = mysql.connect()
    cursor = conn.cursor()
    json_Dict = json.loads(msg.payload)
    data_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    temperature = json_Dict['Temperature']
    cursor.execute("INSERT INTO tbl_temperature(date_time, temperature) VALUES (%s,%s)" ,(data_time, temperature))
    conn.commit()

# Subscribe to topic
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("mqtt")

# Page for load Graphs
@app.route('/')
def hello_world():
    return render_template('index.html', data='test')

# function called from ajax for update graphs
@app.route('/live-data')
def live_data():
    global temperature
    data = [time() * 1000, temperature]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

# Init app
if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("192.168.0.17", 1883, 60)
    client.publish("mqtt", 'publicandooo');
    client.loop_start()
    app.run(host='127.0.0.1', port=port)
