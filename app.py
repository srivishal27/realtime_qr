# server.py
from flask import Flask, request, jsonify, render_template

from pyzbar.pyzbar import decode
import cv2
import numpy as np
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/decode', methods=['POST'])
def decode_frame():
    data = request.get_json()
    frame = data['frame']
    frame = frame.split(',')[1]
    frame = base64.b64decode(frame)
    nparr = np.fromstring(frame, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    codes = decode(img)
    if codes:
        return codes[0].data.decode()
    else:
        return "No QR code detected."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
