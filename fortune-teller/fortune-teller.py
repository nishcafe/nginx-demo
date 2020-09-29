from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def open_cookie():
    m = request.args.get('msg')
    return {'message': "Your fortune cookie says: {}".format(m)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002')


