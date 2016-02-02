from litefb_app import app, browser 
from flask import redirect, url_for, request, render_template

@app.route('/login/panel')
def login():
    browser.open('https://m.facebook.com/')
    lf = browser.get_form(id='login_form')
    if lf is None:
        return redirect(url_for('index'))
    else:
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def loginchk():
    if request.method == 'POST':
        user = request.form['buser']
        passwd = request.form['bpass']
        browser.open('https://m.facebook.com/')
        lf = browser.get_form(id='login_form')
        lf['email'].value = user
        lf['pass'].value = passwd
        browser.submit_form(lf)
        return redirect(url_for('main.index'))
