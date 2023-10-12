import base64
from io import BytesIO
from flask import Flask, request, jsonify
import cv2
import dlib
import requests
import os
import numpy as np 
import urllib.request as urllib

app = Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))
model_name = '/shape_predictor_68_face_landmarks.dat'
model_path = dir_path + model_name

if os.path.exists(model_path) != True:
    print('Could not locate model file, downloading...')
    print('Downloading: ' + model_name)
    urllib.urlretrieve('https://github.com/italojs/facial-landmarks-recognition/raw/master/shape_predictor_68_face_landmarks.dat', model_path)


print('Starting Face Alignment API...')
# Load the face detection and landmark detection models
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(model_path)


@app.route('/detect_face', methods=['GET'])
def detect_face():
    try:
        # Receive the URL of the image from the client
        image_url = request.args.get('image_url')

        # Download the image from the URL
        response = requests.get(image_url)
        image_data = BytesIO(response.content)
        image = cv2.imdecode(np.fromstring(image_data.read(), np.uint8), cv2.IMREAD_COLOR)
        
        # Convert the image to grayscale for face detection
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        faces = detector(gray)

        if len(faces) == 0:
            return jsonify({'error': 'No faces detected'})

        # Find the largest detected face
        largest_face = max(faces, key=lambda rect: (rect.right() - rect.left()) * (rect.bottom() - rect.top()))

        # Extract 68 facial landmarks for the largest face
        landmarks = predictor(gray, largest_face)

         # Align the face using dlib's get_face_chip function
        aligned_face = dlib.get_face_chip(image, landmarks, size=320)

        # Convert the cropped face to a base64-encoded string
        _, buffer = cv2.imencode('.jpg', aligned_face)
        base64_encoded = base64.b64encode(buffer).decode('utf-8')

        return jsonify({'aligned_face_base64': base64_encoded})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)