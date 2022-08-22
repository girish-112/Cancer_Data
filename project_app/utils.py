import pickle
import json
import config
import numpy as np

class CancerData():
    def __init__(self,mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness):
        self.mean_radius = mean_radius
        self.mean_texture = mean_texture
        self.mean_perimeter = mean_perimeter
        self.mean_area = mean_area
        self.mean_smoothness = mean_smoothness
        
    def load_model(self) :
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model =pickle.load(f)
            
        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data =json.load(f)    
    
    def get_cancer_prediction(self):
        self.load_model()
        test_array = np.zeros(len(self.json_data['columns']))
        
        test_array[0] = self.mean_radius
        test_array[1] = self.mean_texture
        test_array[2] = self.mean_perimeter
        test_array[3] = self.mean_area
        test_array[4] = self.mean_smoothness

        predicted_category = np.around(self.model.predict([test_array])[0],2)
        return predicted_category

            
    


