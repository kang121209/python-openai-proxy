from flask import Flask
from flask_cors import CORS
from flask_proxy import Proxy

app = Flask(__name__)
CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>',methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
def proxy(path):
    return Proxy('https://api.openai.com').forward()

if __name__ == '__main__':
    app.run(port=8623)
