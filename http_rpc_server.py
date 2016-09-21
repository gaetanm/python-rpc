from flask import Flask, jsonify, request
import time
import psutil
import json
import dicttoxml

app = Flask(__name__)


@app.route('/time')
def current_timestamp():
    return jsonify(time=int(time.time()))


@app.route('/ram')
def ram_status():
    return jsonify(total=psutil.virtual_memory()[0],
                   used=psutil.virtual_memory()[3])


@app.route('/hdd')
def hdd_status():
    return jsonify(total=psutil.disk_usage('/')[0],
                   used=psutil.disk_usage('/')[1])

@app.route('/add')
def add():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=(a + b))

@app.route('/sub')
def sub():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=(a - b))

@app.route('/json_to_xml')
def json_to_xml():
    json_str = request.args.get('json_str', type=str)
    obj = json.loads(json_str)
    xml = dicttoxml.dicttoxml(obj)
    return jsonify(result=xml)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)
