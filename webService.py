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


# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')

# Add uniform route.
@app.route('/api/uniform')
def uniform():
  return {"value": np.random.uniform()}

# Add normal route.
@app.route('/api/normal')
def normal():
  return {"value": np.random.normal()}