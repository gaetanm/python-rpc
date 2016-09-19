from flask import Flask, jsonify
import time
import psutil

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
    return jsonify(total=psutil.disk_usage("/")[0],
                   used=psutil.disk_usage("/")[1])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
