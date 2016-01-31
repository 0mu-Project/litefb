from setting import FB_APP_ID, FB_APP_SEC
from urllib import parse
import http.client
import json

FB_BASE='https://www.facebook.com/dialog/oauth'
FB_GRAPH_API='graph.facebook.com'

## Reference: https://developers.facebook.com/docs/facebook-login/permissions
FB_SCOPE='public_profile'

def genGetCodeURL(RedirectURL):
    return FB_BASE+'?client_id='+FB_APP_ID+\
            '&scope='+parse.quote_plus(FB_SCOPE)+\
            '&redirect_uri='+parse.quote_plus(RedirectURL)

def getToken(RedirectURL,code):
    conn = http.client.HTTPSConnection(FB_GRAPH_API)
    request='/oauth/access_token'+\
    '?client_id='+FB_APP_ID+\
    '&client_secret='+FB_APP_SEC+\
    '&redirect_uri='+parse.quote_plus(RedirectURL)+\
    '&code='+code
    conn.request("GET", request)
    resault = conn.getresponse()

    data1 = resault.read().decode("utf-8")
    
    if resault.status == 200:
        token=data1.split("&")[0].split('=')[1]
        expir=data1.split("&")[1].split('=')[1]
        
        return [True,token,expir]
    else:
        return [False,data1]

def getInfo(Token):
    conn = http.client.HTTPSConnection(FB_GRAPH_API)
    request='/me?access_token='+Token
    conn.request("GET", request)
    resault = conn.getresponse()

    if resault.status == 200:
        return resault.read().decode("utf-8") 
    else:
        return False


def getUID(Token):
    try:
        JSONdata = getInfo(Token)
        data=json.loads(JSONdata)
        return data['id']
    
    except:
        return False

def getName(Token):
    try:
        JSONdata = getInfo(Token)
        data=json.loads(JSONdata)
        return data['name']
    
    except:
        return False

