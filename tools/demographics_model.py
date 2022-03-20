from pickletools import UP_TO_NEWLINE
from tensorflow import keras
import model_utils
from math import floor, ceil


def load_model():
    model = keras.models.load_model("pretrained/New_32CL_5LR_43Epoc")
    return model

def prepare_output(pred):
    
    # This function will return the final output as a list : [ <GENDER ('M' or 'F')>   ,   <AGE (NUMBER)> ]

    # As the output comes in terms of an age bracket, I am getting the mean of each, 
    # and along with the confidence the model has on each bracket, I calculate the weighted sum of the ages.

    output = []

    # Original age brackets were : '(0-15)','(16-30)','(31-45)','(46-60)','(>60)'
    age_bracks_mean = [8, 23, 36, 48, 70]

    # Calculating the age using a weighted method
    weighted_age = 0

    for i in range(5):
        weighted_age += pred[0][i+2]*age_bracks_mean[i]
    weighted_age = int(floor(weighted_age))
    output.append(weighted_age)


    # To decide M or F
    if pred[0][0]>pred[0][1]:
        output.append("F")
    else:
        output.append("M")


    return output

def give_output(model, frame1):
    frame1 = model_utils.prepare_input_for_demographic(frame1)
    pred = model.predict( [frame1] )
    beautified_pred = prepare_output(pred)
    return beautified_pred
