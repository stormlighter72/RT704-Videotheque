from flask import Flask, abort, render_template
import requests

app_url = "http://app:5000/"

app = Flask(__name__)

@app.get('/')
def response():
    response=requests.get(app_url+"videotheque")
    if response.status_code == 200 :
        return render_template("index.html.jinja", video = response.json())
    elif  response.status_code == 404 :
        abort(response.status_code)

@app.get('/library1')
def Library_1():
    response=requests.get(app_url+"videotheque")
    if response.status_code == 200 :
        return render_template("library.html.jinja", video = response.json())
    elif  response.status_code == 404 :
        abort(response.status_code)
    
@app.get('/library2')
def Library_2():
    response=requests.get(app_url+"videotheque2")
    if response.status_code == 200 :
        return render_template("library2.html.jinja", video = response.json())
    elif  response.status_code == 404 :
        abort(response.status_code)
    
#@app.get('/mozaique')
#def image_index():
    

@app.errorhandler(404)
def error_404(error):
    return render_template("error_404.html.jinja")