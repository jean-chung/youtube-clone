from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    with open('db.json', 'r') as f:
        db = json.load(f)

    return render_template('home.html', db=db)

@app.route('/watch/')
@app.route('/watch/<name>')
def watch(name=None):
    return render_template('watch.html', name=name)