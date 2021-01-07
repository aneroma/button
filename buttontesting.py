#!/usr/bin/python

# Importing necessary libraries for logging and calling an API
import logging
import urllib
import httplib
import sys 


effective_level = logging.getLogger("scapy.runtime").getEffectiveLevel()
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

# Importing the scapy library, which will be used to scan and capture the packet that is sent by the dash button, thus triggering the rest of the code.
from scapy import all
from scapy.all import *

# Dash button mac & Pushover variables
DASH_BUTTON_MAC = '6c:56:97:43:b2:eb'
APP_TOKEN = 'aivnc3qipxqxsqc7e6fv61bzgateb5'
USER_TOKEN = 'uox33y2bz71ofpr87cin4npyo9mfu4'

# This function will call the Pushover API using a POST request to send the tokens and the message, as shown in their API documentation.
def pushover(given_message):
    print 'Sending Pushover API post request...'
    conn = httplib.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
        urllib.urlencode({
            "token": APP_TOKEN,
            "user": USER_TOKEN,
            "html":"0",
            "title":"Doorbell!",
            "message":given_message,
            "sound":"pushover",
        }), { "Content-type": "application/x-www-form-urlencoded" })
    response = conn.getresponse()
    print("Pushover API response status is {}".format(response.status))


# Door sensor code starts here

from sense_hat import SenseHat


sense = SenseHat() 

def door_open():
   while True:
       # Grabbing the raw accelerometer data from the sense hat on the P
       acceleration = sense.get_accelerometer_raw()
       x = acceleration['x']
       y = acceleration['y']
       z = acceleration['z']
   
       # If the Y axis changes, then we assume somebody opened the door because the Pi moved
      

       if int(round(y)) == 1:
          pushover('Somebody opened the door')
          sense.show_message("Door is open!", text_colour=[0, 0, 255], back_colour=[255, 255, 0], scroll_speed=0.08) 
          sense.clear()

          temp = sense.get_temperature()
          humidity = sense.get_humidity()
          pressure = sense.get_pressure()
          message = 'Temperature is %d Humidity is %d Pressure is %d mbars'%(temp,humidity,pressure)
          sense.show_message(message, scroll_speed=(0.08),text_colour=[255, 255, 0], back_colour=[0, 0, 255])
          sense.clear()


# Creating a function that gets called by scapy in the 'sniff' function to act as a filter for each packet we detect
def udp_filter(pkt):
    if pkt.haslayer(DHCP):
       if pkt[Ether].src == DASH_BUTTON_MAC:
          pushover('Someone is at the door')

def button_push():
   sniff(prn=udp_filter, store=0, filter="udp")

from multiprocessing import Process

try:
   print('Ready!')
   process1 = Process(target=door_open)
   process1.start()
   process2 = Process(target=button_push)
   process2.start()
except Exception as e:
   # Uncomment next line for debugging
   # print(e)
   process1.close()
   process1.join()
   process2.close()
   process2.join()
   print('Closing...')
