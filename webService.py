# Author     : Tomas O'Malley
# Student ID : G00361128 (@gmit.ie)
# Course     : Software Development GA_KSOAG_H08 Y4
# Module     : Emerging Technologies
# Program    : WebService python application
# Due Date 	 : 08/01/2021

# flask for web app imports .
import flask as fl
from flask import request
import tensorflow as tf

#Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
    return app.send_static_file('index.html')

@app.route("/powerOut", methods=["POST"])
def powerOutput():
    windSpeed = float(request.get_json()["value"]) #gets wind speed input from websercive.py
    model=tf.keras.models.load_model("powerProduction.h5")#gets data model from powerProduction created in journal
    prediction = model.predict([windSpeed]) #get prediction using data model & wind speed user  input
    predList = prediction.tolist() # convert prediciton to a type  list
    return {'prediction':predList[0]} #retrive  first element of prediction list and display
if __name__== '__main__':
    app.run(debug=True)
