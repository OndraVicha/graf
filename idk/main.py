
from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/graph')
def graph():
    return render_template('graph.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)