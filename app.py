from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permet les requêtes cross-origin

# Endpoint pour analyser l'URL YouTube
@app.route("/analyze", methods=["POST"])  # Méthode POST
def analyze():
    data = request.get_json()  # Récupère les données JSON envoyées
    if not data or "youtube_url" not in data:
        return jsonify({"error": "Missing youtube_url"}), 400  # Si l'URL YouTube est manquante

    youtube_url = data["youtube_url"]
    # Ajouter la logique d'analyse ici (par exemple, vérifier si la vidéo existe sur TikTok)
    result = {"message": f"Analyzing {youtube_url}"}

    return jsonify(result)  # Retourne un résultat sous forme de JSON

if __name__ == "__main__":
    app.run(debug=True)

from pytube import YouTube
import cv2
import librosa
import os
os.system("git clone https://github.com/dpwe/audfprint.git && cd audfprint && python setup.py install")
import audfprint
import audfprint
import requests
import os

app = Flask(__name__)

# 🔽 Télécharger la vidéo YouTube
def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    file_path = "youtube_audio.mp3"
    stream.download(filename=file_path)
    return file_path

# 🔊 Analyse Audio
def get_fingerprint(audio_path):
    y, sr = librosa.load(audio_path)
    return audfprint.compute_fingerprint(y, sr)

# 🕵️‍♂️ Scraping TikTok (exemple simplifié)
def search_tiktok(query):
    response = requests.get(f"https://www.tiktok.com/search?q={query}")
    return ["https://www.tiktok.com/@exemple/video/123456789"]  # Simulation

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    video_url = data.get("video_url")
    
    if not video_url:
        return jsonify({"error": "Lien YouTube manquant"}), 400

    # 🔽 Télécharger et analyser la vidéo
    audio_file = download_video(video_url)
    fingerprint = get_fingerprint(audio_file)
    
    # 🔎 Chercher sur TikTok
    tiktok_results = search_tiktok(YouTube(video_url).title)
    
    return jsonify({
        "score": 85,  # Score simulé
        "found": bool(tiktok_results),
        "tiktok_links": tiktok_results
    })

if __name__ == '__main__':
    app.run(debug=True)
