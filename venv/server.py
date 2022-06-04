from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

class Video:
    def __init__(self, name, video):
        self.name = name
        self.video = video

@app.route("/")
def home():
    videoList = []
    with open('db.json', 'r') as f:
        db = json.load(f)
    for name, video in db.items():
        videoList.append(Video(name, video))
    return render_template('home.html', videoList=videoList)

@app.route('/watch/')
@app.route('/watch/<name>')
def watch(name=None):
    return render_template('watch.html', name=name)