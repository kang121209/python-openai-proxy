#-*-coding:utf-8-*-
from flask import Flask
from flask_http_proxy_middleware import HTTPProxyMiddleware

app = Flask(__name__)
app.config["PROXY_MIDDLEWARE_URL"] = "https://api.openai.com"
app.config["PROXY_MIDDLEWARE_HEADERS"] = {"Access-Control-Allow-Origin": "*"}
app.config["PROXY_MIDDLEWARE_HOSTS"] = ("*",)

http_proxy_middleware = HTTPProxyMiddleware(app)

@app.route("/")
def proxy():
    return http_proxy_middleware.handle_request()

if __name__ == "__main__":
    app.run(port=9000)

