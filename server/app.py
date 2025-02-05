#################################################################
# Temperature_API.py
#
# copyright
# August 2019
#
# Simon Little
# Rich Little
#
# This module runs the server code recieving sensor readings
# being uploaded to (outside, inside, slab) files.
# This module handles POST requests made by the clients and saves
# it to csv
#################################################################

from flask import Flask, request, jsonify, abort, send_file
import pandas as pd
import csv
import subprocess
import socket

app = Flask(__name__)


@app.route('/datanode', methods=['POST'])
def index():
    if request.method == 'POST':
        json = request.get_json(force=True)
        df = pd.DataFrame([json['temp']], index=[json['time']])
        df.to_csv(request.args['node'] + '.csv', mode='a', header=False)
        return jsonify(json), 201


@app.route('/<string:table>.csv', methods=['GET'])
def getter(table):
        if request.method == 'GET':
            reader = csv.DictReader(open(table+'.csv'))  
            # Parse the CSV into JSON  
            out = jsonify( [ row for row in reader ] ) 
            print(out)
            return out, 200, {}

interface = "wlan0"
try:
	ip = str(subprocess.check_output("ifconfig " + interface + " | grep 'inet'| cut -d':' -f2", shell = True).strip())
	ip = ip[ip.find('192'):ip.find('192')+12]
except:
	ip=socket.gethostnamebyname(socket.gethostname())	
print(ip)
app.run(host=ip)
