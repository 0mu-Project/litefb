from litefb_app import app 
import logging, setting
from litefb_app.index import main
from litefb_app.login import login
from werkzeug.contrib.fixers import ProxyFix 

app.secret_key = setting.yourkey
app.wsgi_app = ProxyFix(app.wsgi_app)
app.register_blueprint(main)

if __name__ == '__main__':
    logging.basicConfig(filename=setting.s_log, level=logging.DEBUG)
    print('0MuMDAU Server Run on ' + str(setting.host) + ':' + str(setting.port))
    if setting.debug == 0:
        debugB = False 
    else:
        debugB = True
        print('fuu')
    app.run(host=str(setting.host), port=setting.port, debug=debugB)
