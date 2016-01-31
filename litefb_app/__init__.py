# -*- coding: utf-8 -*-

from flask import Flask, request

app = Flask(__name__)

def restart_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/restart')
def restart():
    restart_server()
