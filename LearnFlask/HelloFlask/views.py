from datetime import datetime
from flask import render_template, redirect, url_for
from HelloFlask import app

@app.route('/')
@app.route('/home')
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %B %d, %Y at %X")

    return render_template(
        "index.html",
        title = "Hello Flask",
        message = "Hello, all you glorious bastards!",
        content = " on " + formatted_now)

@app.route('/about')
def about():
    return render_template(
        "about.html",
        title = "About HelloFlask",
        content = "Example app page for Visaul Studio Docs Flask tutorial."
        )

@app.route('/api/data')
def get_data():
    return app.send_static_file('data.json')