# Author     : Tomas O'Malley
# Student ID : G00361128 (@gmit.ie)
# Course     : Software Development GA_KSOAG_H08 Y4
# Module     : Emerging Technologies
# Program    : WebService python application
# Due Date 	 : 08/01/2021

# flask for web app.
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
    windSpeed = float(request.get_json()["value"]) #gets wind speed input from index.htmlk
    model=tf.keras.models.load_model("powerprod.h5")#gets data model from
    prediction = model.predict([windSpeed]) #get prediction using data model & wind speed input
    predList = prediction.tolist() # convert prediciton to list
    return {'prediction':predList[0]} #get first element of prediction list
if __name__== '__main__':
    app.run(debug=True)
    #time 30.05
