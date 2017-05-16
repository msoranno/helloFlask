from flask import Flask

app = Flask(__name__)


@app.route('/')
def helloFlask():
    return '<h2>hello flask</h2>'


if __name__ == '__main__':
    app.run(debug=True)
