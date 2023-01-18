from flask import Flask, abort, request
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


@app.get('/addfilm', methods = ['POST'])
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
        videotheque = None

        with open('video.json') as videotheque_file :
                videotheque = json.load(videotheque_file)
                videotheque["films"].append({"titre":titre,"annee":annee, "realisateur":{"nom":nom_realisateur,"prenom":prenom_realisateur},"acteurs":[{"nom":nom_acteur1,"prenom":prenom_acteur1},{"nom":nom_acteur2,"prenom":prenom_acteur2},{"nom":nom_acteur3,"prenom":prenom_acteur3}]})
        with open('video.json','w+') as videotheque_file:
                json.dump(videotheque, videotheque_file, indent=4)
                return "Ok niquel"
        
