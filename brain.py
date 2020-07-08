import pickle
import numpy as np
from keras.models import load_model


def brain(x):
    model = load_model('model.h5')
    with open('cv.pkl', 'rb') as file:
        cv = pickle.load(file)
        x = cv.transform([x])
        pred = model.predict(x)
        if(pred > 0.5):
            return 1
        else:
            return 0