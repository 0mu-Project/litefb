# -*- coding: utf-8 -*-

from flask import Flask, request
from robobrowser import RoboBrowser
browser = RoboBrowser(history=True, user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0')
app = Flask(__name__)

def restart_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/restart')
def restart():
    restart_server()
