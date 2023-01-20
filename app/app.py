from flask import Flask, abort, request, redirect, url_for
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

@app.get('/videotheque2')
def open_read2():
        if os.path.exists('video2.json'):
                with open('video2.json') as videotheque_file2 :
                        videos2 = json.load(videotheque_file2)
        else:
                abort(404)
        return videos2


@app.post('/addfilm')
def AddFilm():
        titre = request.json['titre']
        annee = request.json['annee']
        nom_realisateur = request.json['nom_realisateur']
        prenom_realisateur = request.json['prenom_realisateur']
        nom_acteur1 = request.json['nom_acteur1']
        nom_acteur2 = request.json['nom_acteur2']
        nom_acteur3 = request.json['nom_acteur3']
        prenom_acteur1 = request.json['prenom_acteur1']
        prenom_acteur2 = request.json['prenom_acteur2']
        prenom_acteur3 = request.json['prenom_acteur3']
        videotheque = None

        with open('video.json') as videotheque_file :
                videotheque = json.load(videotheque_file)
                videotheque["films"].append({"titre":titre,"annee":annee, "realisateur":{"nom":nom_realisateur,"prenom":prenom_realisateur},"acteurs":[{"nom":nom_acteur1,"prenom":prenom_acteur1},{"nom":nom_acteur2,"prenom":prenom_acteur2},{"nom":nom_acteur3,"prenom":prenom_acteur3}]})
        with open('video.json','w+') as videotheque_file:
                json.dump(videotheque, videotheque_file, indent=4)
                return "Ok"
        
@app.post('/addfilm2')
def AddFilm2():
        titre = request.json['titre']
        annee = request.json['annee']
        nom_realisateur = request.json['nom_realisateur']
        prenom_realisateur = request.json['prenom_realisateur']
        nom_acteur1 = request.json['nom_acteur1']
        nom_acteur2 = request.json['nom_acteur2']
        nom_acteur3 = request.json['nom_acteur3']
        prenom_acteur1 = request.json['prenom_acteur1']
        prenom_acteur2 = request.json['prenom_acteur2']
        prenom_acteur3 = request.json['prenom_acteur3']
        videotheque = None

        with open('video2.json') as videotheque_file :
                videotheque = json.load(videotheque_file)
                videotheque["films"].append({"titre":titre,"annee":annee, "realisateur":{"nom":nom_realisateur,"prenom":prenom_realisateur},"acteurs":[{"nom":nom_acteur1,"prenom":prenom_acteur1},{"nom":nom_acteur2,"prenom":prenom_acteur2},{"nom":nom_acteur3,"prenom":prenom_acteur3}]})
        with open('video2.json','w+') as videotheque_file:
                json.dump(videotheque, videotheque_file, indent=4)
                return "Ok"
        
@app.post('/library1')
def DelFilm():
        titre = request.json['titre']
        videotheque = None

        with open('video.json') as videotheque_file :
                videotheque = json.load(videotheque_file)
                index = next((i for i, film in enumerate(videotheque['films']) if film['titre'] == titre), None)
                if index is not None :
                        del videotheque['films'][index]
                else :
                        abort(404) 
        with open('video.json','w+') as videotheque_file:
                json.dump(videotheque, videotheque_file, indent=4)
                return "Ok"

@app.route("/modiffilm")
def modif():
    titre = request.args.get("titre")
    with open("video.json") as videotheque_file:
        videotheque = json.load(videotheque_file)
        film = next((film for film in videotheque['films'] if film['titre'] == titre), None)

    if film:
        return film
    else:
        return jsonify({"error": "Film not found"})

@app.route("/mod",methods=['POST'])
def mod():
    titre_base = request.json['titre_base']
    titre = request.json['titre']
    annee = request.json['annee']
    nom_realisateur = request.json['nom_realisateur']
    prenom_realisateur = request.json['prenom_realisateur']
    nom_acteur1 = request.json['nom_acteur1']
    nom_acteur2 = request.json['nom_acteur2']
    nom_acteur3 = request.json['nom_acteur3']
    prenom_acteur1 = request.json['prenom_acteur1']
    prenom_acteur2 = request.json['prenom_acteur2']
    prenom_acteur3 = request.json['prenom_acteur3']
    with open('video.json', 'r') as videotheque_file :
        videotheque = json.load(videotheque_file)
        for i, film in enumerate(videotheque['films']):
            if titre_base == film['titre']:
                del videotheque['films'][i]
                break
    with open('video.json','w+') as videotheque_file:
        json.dump(videotheque, videotheque_file, indent=4)
    with open('video.json') as videotheque_file :
        videotheque = json.load(videotheque_file)
        videotheque["films"].append({"titre":titre,"annee":annee, "realisateur":{"nom":nom_realisateur,"prenom":prenom_realisateur},"acteurs":[{"nom":nom_acteur1,"prenom":prenom_acteur1},{"nom":nom_acteur2,"prenom":prenom_acteur2},{"nom":nom_acteur3,"prenom":prenom_acteur3}]})
    with open('video.json','w+') as videotheque_file:
        json.dump(videotheque, videotheque_file, indent=4)
        return "Ok niquel"