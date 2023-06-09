import flask
import io
import string
import time
import os
import numpy as np
import tensorflow as tf
from PIL import Image
from flask import Flask, jsonify, request

model = tf.keras.models.load_model('models/1')
models = tf.keras.models.load_model('modelss/1')

def prepare_image(img):
    img = Image.open(io.BytesIO(img)).convert('RGB')
    img = img.resize((150, 150))
    img = np.array(img)
    img = np.expand_dims(img, 0)
    return img

def prepare_images(imgs):
    imgs = Image.open(io.BytesIO(imgs)).convert('RGB')
    imgs = imgs.resize((224, 224))
    imgs = np.array(imgs)
    imgs = np.expand_dims(imgs, 0)
    return imgs

def predict_result_alzheimer(img):
    return "Pneumonia" if model.predict(img)[0][0] > 0.5 else "Normal"


def predict_result_lung(imgs):
    if models.predict(imgs)[0][0] > 0.5:
        return "Benign"
    elif models.predict(imgs)[0][1] > 0.5:
        return  "Malignant"
    elif models.predict(imgs)[0][2] > 0.5:
        return "normal"
    else :
        return "CT-Scan Tidak Dapat di Prediksi"


app = Flask(__name__)

@app.route('/predict_disease', methods=['POST'])
def infer_image():
    if 'file' not in request.files:
        return "Please try again. The Image doesn't exist"
    
    file = request.files.get('file')

    if not file:
        return

    img_bytes = file.read()
    img = prepare_image(img_bytes)
    imgs = prepare_images(img_bytes)

    return jsonify(prediction=predict_result_alzheimer(img))
    return jsonify(prediction=predict_result_lung(img))


# @app.route('/lung', methods=['POST'])
# def infer_images():
#     if 'file' not in request.files:
#         return "Please try again. The Image doesn't exist"
    
#     file = request.files.get('file')

#     if not file:
#         return

#     img_bytes = file.read()
#     img = prepare_images(img_bytes)

#     return jsonify(prediction=predict_result_lung(img))
    

@app.route('/', methods=['GET'])
def index():
    return 'Machine Learning Inference'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')