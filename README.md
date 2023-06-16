<p align='center'>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />        
  </a>&nbsp;&nbsp;
  <a href="https://flask.palletsprojects.com/en/2.0.x/">
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />        
  </a>&nbsp;&nbsp;
  <a href="https://www.tensorflow.org/">
    <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" />
  </a>&nbsp;&nbsp;
   <a href="https://keras.io/">
    <img src="https://img.shields.io/badge/Keras-880808?style=for-the-badge&logo=keras&logoColor=white" />
  </a>&nbsp;&nbsp;
</p>
<br>

## Bangkit Capstone Project 2023
Bangkit Capstone Team ID : C23-PS011 <br>
Here is our repository for Bangkit 2023 Capstone project - Machine Learning

## Machine Learning Schedule
|     Week 1     |       Week 2        |            Week 3          |           Week 4          |
| :------------: | :-----------------: | :------------------------: |:------------------------: |
| Searching and collecting dataset   | Dataset validation and cleaning      | Selection of Machine Learning method  | Model deployment  |

## Datasets
The project utilizes the following datasets for training the machine learning models:
* [Lung Cancer Dataset](https://www.kaggle.com/datasets/waseemnagahhenes/lung-cancer-dataset-iq-othnccd)
* [CT Scan Image Dataset](https://www.kaggle.com/datasets/iashiqul/brain-stroke-prediction-ct-scan-image-dataset)
* [Alzheimer's Dataset](http://kaggle.com/datasets/tourist55/alzheimers-dataset-4-class-of-images)
* [Custom Dataset Wound Prediction](https://drive.google.com/file/d/1fnkYzOJUuO-K7Mh2c_i0LxgjVUeSkt3W/view?usp=sharing)

## About Model
The model is created using Tensorflow and Keras Library then uses CNN to create a neural network after which the model will be trained and predict the training results. The model trained is a model regarding the prediction of Alzheimer's disease and Cancer Disease. The Alzheimer's model uses image_size (150,150) while the Cancer model uses image_size (224,224) where each of these datasets has 3 colors, namely RGB.Then this model uses a callback when the accuracy has reached 85%.Then after the model is successfully trained then the model will be tested.After that the model will be saved and an API will be created so that it can be deployed and can be used on Mobile.


![Testing Model](https://i.ibb.co/7j3KWnC/Screenshot-80.png)

## Tools and Technologies
The following tools and technologies are utilized in this project:
* Python
* TensorFlow
* Google Collab
* Kaggle
* Scikit-Learn
* Matplotlib

## Deployment And How To Run This Model
1. Create Model Machine Learning and saved the model
2. install flask as a framework for creating Machine Learning Model APIs
3. create folders to hold Flask files and Machine Learning models
4. Install ENV in python 
5. Import the required libraries.
6. Running the flask code that has been created in app.py

   <choose folder> flask run
   
8. Testing on Postman whether the model was successfully converted into an API.

![API ML](https://i.ibb.co/PQWXHKf/Screenshot-79.png)


