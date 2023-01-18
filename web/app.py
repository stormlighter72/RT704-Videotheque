from flask import Flask, abort, render_template, request
import requests

app_url = "http://app:5000/"

app = Flask(__name__)

@app.get('/')
def response():
    response=requests.get(app_url+"videotheque")
    if response.status_code == 200 :
        return render_template("index.html.jinja", video = response.json())
    else :
        abort(response.status_code)

@app.get('/library1')
def Library_1():
    response=requests.get(app_url+"videotheque")
    if response.status_code == 200 :
        return render_template("library.html.jinja", video = response.json())
    else:
        abort(response.status_code)
    
@app.get('/library2')
def Library_2():
    response=requests.get(app_url+"videotheque2")
    if response.status_code == 200 :
        return render_template("library2.html.jinja", video = response.json())
    else:
        abort(response.status_code)

@app.get('/addfilm')
def AddFilm():
    titre = request.json['titre']
    annee = request.json['annee']
    nom_realisateur = request.json['nom_real']
    prenom_realisateur = request.json['prenom_real']
    nom_acteur1 = request.json['nom_acteur1']
    nom_acteur2 = request.json['nom_acteur2']
    nom_acteur3 = request.json['nom_acteur3']
    prenom_acteur1 = request.json['prenom_acteur1']
    prenom_acteur2 = request.json['prenom_acteur2']
    prenom_acteur3 = request.json['prenom_acteur3']
    
    response = requests.post(app_url, json={"titre":titre, "annee":annee, "nom_realisateur":nom_realisateur, "prenom_realisateur":prenom_realisateur, "nom_acteur1":nom_acteur1, "prenom_acteur1":prenom_acteur1, "nom_acteur2":nom_acteur2, "prenom_acteur2":prenom_acteur2, "nom_acteur3":nom_acteur3, "prenom_acteur3":prenom_acteur3,})
    if response.status_code == 200 :
        return response
    else:
        return response
    

@app.errorhandler(404)
def error_404(error):
    return render_template("error_404.html.jinja")