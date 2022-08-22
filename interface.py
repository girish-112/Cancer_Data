import re
from flask import Flask,jsonify,request
from project_app.utils import CancerData
import config

app=Flask(__name__)

@app.route('/')
def home_api():
    return "Welcome to Medical data Prediction"


@app.route('/predict_can')
def get_patient_details():
    data = request.form 
    
    
    mean_radius = eval(data['mean_radius'])
    mean_texture = eval(data['mean_texture'])
    mean_perimeter = eval(data['mean_perimeter'])
    mean_area = eval(data['mean_area'])
    mean_smoothness = eval(data['mean_smoothness'])
    
    
    diesease_p = CancerData(mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness)
    predict=diesease_p.get_cancer_prediction()
    return jsonify({"Patient diabetes evaluation =":f"{predict}"})    
    
if __name__=='__main__':
    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=False)
    
    
    
    
    
