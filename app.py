from flask import Flask

app = Flask(__name__)


@app.route('/')
def base_route():
    return {"asd": 123}, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
