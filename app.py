from flask import Flask

app = Flask(__name__)


@app.route('/')
def foo():
    return 'Melo Susik'


if __name__ == '__main__':
    app.run(debug=True)
