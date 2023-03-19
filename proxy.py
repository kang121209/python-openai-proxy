#-*-coding:utf-8-*-
import os
from flask import Flask,request, Response,api
from flask_cors import CORS
import requests  # pip package requests
app = Flask(__name__)
CORS(app)

API_HOST='https://api.openai.com'

@api.route('/', defaults={'path': ''})  
@api.route('/<path>')
def redirect_to_API_HOST(path): 
    res = requests.request(  
        method          = request.method,
        url             = request.url.replace(request.host_url, f'{API_HOST}/'),
        headers         = {k:v for k,v in request.headers if k.lower() == 'host'},
        data            = request.get_data(),
        cookies         = request.cookies,
        allow_redirects = False,
    )

    #region exlcude some keys in :res response
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']  #NOTE we here exclude all "hop-by-hop headers" defined by RFC 2616 section 13.5.1 ref. https://www.rfc-editor.org/rfc/rfc2616#section-13.5.1
    headers          = [
        (k,v) for k,v in res.raw.headers.items()
        if k.lower() not in excluded_headers
    ]
    #endregion exlcude some keys in :res response

    response = Response(res.content, res.status_code, headers)
    return response

    
