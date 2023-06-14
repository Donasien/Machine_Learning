import flask
import io
import string
import time
import os
import numpy as np
import tensorflow as tf
from PIL import Image
from flask import Flask, jsonify, request

import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
host = os.getenv('DB_HOST')

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
        return "Normal"
    else :
        return "CT-Scan Tidak Dapat di Prediksi"


app = Flask(__name__)

@app.route('/predict-disease', methods=['POST'])
def infer_image():
    if 'token' not in request.form:
        js = {
            "message": "Token Required",
        }

        return jsonify(js)

    if 'file' not in request.files:
        js = {
            "message": "Image Required",
        }

        return jsonify(js)
    
    token = request.form.get('token')

    cnx = pymysql.connect(user=db_user, password=db_password, host=host, db=db_name)
    
    with cnx.cursor() as cursor:
        cursor.execute("select * from users where token='"+token+"';")
        result = cursor.fetchall()
    cnx.close()

    if not result:
        js = {
            "message": "Token Not Found",
        }

        return jsonify(js)
    
    file = request.files.get('file')

    if not file:
        return

    img_bytes = file.read()
    img = prepare_image(img_bytes)
    imgs = prepare_images(img_bytes)

    js = {
            "prediction_alzheimer": predict_result_alzheimer(img),
            "prediction_lung": predict_result_lung(imgs),
        }

    return jsonify(js)

@app.route('/', methods=['GET'])
def index():
    return 'Machine Learning Donasien'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
