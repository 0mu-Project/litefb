from litefb_app import app 
from flask import session,redirect,url_for,request,render_template,make_response
import sqlite3,hashlib
import facebook

@app.route('/login')
def login():
    code = request.args.get('code',False)
    if not code:
        if not session['fbToken']:
            ## 登入第一階段：前往FB的登入連結
            LoginURL=facebook.genGetCodeURL(request.base_url)
            return '您尚未登入，<a href=\"'+LoginURL+'\">使用facebook登入</a>'
            
        else:
            ## 第三階段，拿Token亂玩
            UID=facebook.getUID(session['fbToken'])
            Name=facebook.getName(session['fbToken'])
            return "Already Login: "+Name+' , your FacebookID is '+UID

    else:
        ## 第二階段：Facebook會把Code送回來，伺服器端要再利用Code取得Token
        Res=facebook.getToken(request.base_url,code)
        if Res[0]:
            ## 到這裡取得Facebook的Token後，準備存入Session
            ## Token的過其時間是Res[2], 單位是秒，過期資訊還沒寫進Session
            session['fbToken'] = Res[1]
            return make_response("正在將Token寫入Session。")
            
        else:
            return "登入失敗，請重試，錯誤訊息："+Res[1]
