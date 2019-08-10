
from flask import Flask, request, jsonify, abort, send_file
import pandas as pd
import csv
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

app.run(host= socket.gethostbyname(socket.gethostname()))
