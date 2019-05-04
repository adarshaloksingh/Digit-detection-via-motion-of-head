import os

#=============PART:1: Taking input image from camera =================
os.system(" python camera_input.py")

#==============PART:2: Doing morphological operations on image ================
os.system(" python morph.py")


#==============PART:3: Predicting the digit using trained model================
os.system(" python digit_prediction.py")
