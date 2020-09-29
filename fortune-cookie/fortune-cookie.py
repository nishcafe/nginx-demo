
from flask import Flask
import fortune_cookie

app = Flask(__name__)

@app.route('/')
def get_fortune():
    return {'message': fortune_cookie.fortune()}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')