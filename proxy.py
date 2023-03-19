#-*-coding:utf-8-*-
import os
from flask import Flask,request as req, Response
from flask_cors import CORS
import requests  # pip package requests
app = Flask(__name__)
CORS(app)

API_HOST='https://api.openai.com/'

@app.route('/', defaults={'path': ''})  
@app.route('/path:path')
def redirect_to_API_HOST(path): 
    print(path,1111111111111)
    method          = 'POST'
    url             = API_HOST + path
    headers         = {"Authorization" : "Bearer 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","Content-Type: application/json"}
    data            = req.get_data()
    cookies         = req.cookies
    print('wwwwwwwwwwwwwww',method,url,headers,data,cookies)
    res = requests.request(  
        method,
        url,
        headers,
        data,
        cookies,
        allow_redirects = False,
    )

    #region exlcude some keys in :res response
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']  #NOTE we here exclude all "hop-by-hop headers" defined by RFC 2616 section 13.5.1 ref. https://www.rfc-editor.org/rfc/rfc2616#section-13.5.1
    headers          = [
        (k,v) for k,v in res.raw.headers.items()
        if k.lower() not in excluded_headers
    ]
    #endregion exlcude some keys in :res response
    print(22222,res.content,res.status_code,headers)
    response = Response(res.content, res.status_code, headers)
    return response
    
if __name__ == '__main__':
    
    app.run(debug=True)
