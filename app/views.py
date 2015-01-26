from app import app
from flask import render_template, request, redirect
from app.libs import UrlShorter

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/u/<short_str>')
def to_long_url(short_str):
    shorter = UrlShorter()
    url = shorter.get_long_url(short_str)
    return redirect(url)

@app.route('/short', methods=['POST'])
def short():
    shorter = UrlShorter()
    url = shorter.gen_short_url(request.form['u'])
    return url