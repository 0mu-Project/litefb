# -*- coding: utf-8 -*-

from flask import render_template, Blueprint
from robobrowser import RoboBrowser
browser = RoboBrowser(history=True, user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0')
user = ''
passwd = ''

main = Blueprint('main', __name__)

@main.route('/')
def index():
    browser.open('https://m.facebook.com/')
    lf = browser.get_form(id='login_form')
    if lf is None:
        f = open('./litefb_app/templates/test.html', 'w') 
        f.write(str(browser.find('div', {'id': 'm_newsfeed_stream'})))
    else:
        lf['email'].value = user
        lf['pass'].value = passwd
        browser.submit_form(lf)
        f = open('./litefb_app/templates/test.html', 'w') 
        f.write(str(browser.find('div', {'id': 'm_newsfeed_stream'})))
    return render_template('index.html')
