from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', data=[])

@app.route('/contributions')
def contributions():
    return render_template('contributions.html', data=[])

if __name__ == '__main__':
    app.run(debug=True)
