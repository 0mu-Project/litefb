# -*- coding: utf-8 -*-

from flask import render_template, Blueprint, url_for, redirect, request
from litefb_app import browser
main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        browser.open('https://m.facebook.com/')
        lf = browser.get_form(id='login_form')
        if lf is not None:
            return redirect(url_for('login'))
        else:
            return render_template('index.html')
    else:
        browser.open('https://m.facebook.com/')
        return str(browser.find('div', {'id': 'm_newsfeed_stream'}))
