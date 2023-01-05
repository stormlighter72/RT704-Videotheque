from flask import Flask, abort
import json
import os

app = Flask(__name__)

@app.get('/videotheque')
def open_read():
        if os.path.exists('video.json'):
                with open('video.json') as videotheque_file :
                        videos = json.load(videotheque_file)
        else:
                abort(404)
        return videos
"""
@app.get('/videotheque2')
def open_read():
        if os.path.exists('video2.json'):
                with open('video2.json') as videotheque_file :
                        videos = json.load(videotheque_file)
        else:
                abort(404)
        return videos
"""