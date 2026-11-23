import os 
from flask import Flask,jsonify

app = Flask(__name__)

MESSAGE= os.environ.get("MESSAGE","Bonjour depuis mon premier PaaS!") 

@app.route("/")
def home():
    return f"<h1>{MESSAGE}</h1><p>Version 2</p>"

@app.route("/api/health")
def health():
    return jsonify(status="ok)

if __name__== "__main__":
    # Utilisé uniquement en local ; en production, c'est gunicorn qui lance l'app
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
