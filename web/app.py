from flask import Flask, abort, render_template, request, redirect, url_for
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

@app.route('/addfilm', methods = ["GET", "POST"])
def AddFilm():
    if request.method == "GET" :
        return render_template("addfilm.html.jinja")
    
    else:
        titre = request.form['titre']
        annee = request.form['annee']
        nom_realisateur = request.form['nom_realisateur']
        prenom_realisateur = request.form['prenom_realisateur']
        nom_acteur1 = request.form['nom_acteur1']
        nom_acteur2 = request.form['nom_acteur2']
        nom_acteur3 = request.form['nom_acteur3']
        prenom_acteur1 = request.form['prenom_acteur1']
        prenom_acteur2 = request.form['prenom_acteur2']
        prenom_acteur3 = request.form['prenom_acteur3']
    
        response = requests.post(app_url+"addfilm", json={"titre":titre, "annee":annee, "nom_realisateur":nom_realisateur, "prenom_realisateur":prenom_realisateur, "nom_acteur1":nom_acteur1, "prenom_acteur1":prenom_acteur1, "nom_acteur2":nom_acteur2, "prenom_acteur2":prenom_acteur2, "nom_acteur3":nom_acteur3, "prenom_acteur3":prenom_acteur3,})
        if response.status_code == 200 :
            return redirect(url_for("Library_1"))
        else:
            return response.text
    
    
@app.route('/addfilm2', methods = ["GET", "POST"])
def AddFilm2():
    if request.method == "GET" :
        return render_template("addfilm2.html.jinja")
    
    else:
        titre = request.form['titre']
        annee = request.form['annee']
        nom_realisateur = request.form['nom_realisateur']
        prenom_realisateur = request.form['prenom_realisateur']
        nom_acteur1 = request.form['nom_acteur1']
        nom_acteur2 = request.form['nom_acteur2']
        nom_acteur3 = request.form['nom_acteur3']
        prenom_acteur1 = request.form['prenom_acteur1']
        prenom_acteur2 = request.form['prenom_acteur2']
        prenom_acteur3 = request.form['prenom_acteur3']
    
        response = requests.post(app_url+"addfilm2", json={"titre":titre, "annee":annee, "nom_realisateur":nom_realisateur, "prenom_realisateur":prenom_realisateur, "nom_acteur1":nom_acteur1, "prenom_acteur1":prenom_acteur1, "nom_acteur2":nom_acteur2, "prenom_acteur2":prenom_acteur2, "nom_acteur3":nom_acteur3, "prenom_acteur3":prenom_acteur3,})
        if response.status_code == 200 :
            return redirect(url_for("Library_2"))
        else:
            return response.text
    

@app.errorhandler(404)
def error_404(error):
    return render_template("error_404.html.jinja")