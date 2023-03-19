#-*-coding:utf-8-*-
from flask import Flask, request, Response
import requests

app = Flask(__name__)

TARGET_HOST='https://api.openai.com'

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def proxy(path):
    target_url = f'{TARGET_HOST}/{path}'
    headers = {key: value for (key, value) in request.headers if key != 'Host'}
    method=request.method
    url=target_url
    data=request.get_data()
    params=request.args
    cookies=request.cookies
    print(target_url,headers,method,url,data,params,cookies)
    response = requests.request(method=request.method,
        url=target_url,
        data=request.get_data(),
        params=request.args,
        headers=headers,
        cookies=request.cookies,
        allow_redirects=False)

    response_headers = [(name, value) for (name, value) in response.raw.headers.items()]
    response_headers.append(('Access-Control-Allow-Origin', '*'))

    response = Response(response.content, response.status_code, response_headers)

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

