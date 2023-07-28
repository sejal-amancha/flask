from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Flask'

@app.route('/product')
def product():
    return 'This is Product page'

if __name__ == "__main__":
    app.run(debug=True)