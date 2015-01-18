from app import app
from flask import render_template, request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/short', methods=['POST'])
def short():
    url = request.form['u']
    return url