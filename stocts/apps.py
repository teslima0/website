from django.apps import AppConfig
from django.conf import Settings
import os
import joblib


class HomeConfig(AppConfig):
    name = 'home'

class HomeanalysisConfig(AppConfig):
   
    paths='C:/Users/TAMAR/Desktop/djanjo3/stocts/home/models/saved_steps1.joblib'

    #path=("C:\Users\TAMAR\Desktop\djanjo3\stocts\home", 'saved_step2.joblib')

    with open(paths, 'rb') as file:
        data= joblib.load(file)

    model_loaded = data['model']
    vectorizer = data['vectorizer']
