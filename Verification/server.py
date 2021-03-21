from hashlib import sha256
import json
import time
from flask import Flask, request
import requests

app = Flask(__name__)

peers = set()

@app.route('/verify', methods=['GET'])
def verification():
    from face_reco_webcam import val
    val_1 = val
    val = "Mismatch"
    return json.dumps({"Authenticated": val_1})

