from flask import Flask, request, jsonify
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
