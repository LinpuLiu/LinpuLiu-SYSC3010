import urllib.request
import requests
import httplib
import threading
import json


def read_data_thingspeak() :
       URL = 'https://api.thingspeak.com/channels/1161204/fields/1.json?api_key='
       KEY =  'BTO7X06U644MHJ6D'
       HEADER = '&result2'
       NEW_URL = URL + KEY + HEADER
       #print (NEW_URL)
       
       get_data = requests.get (NEW_URL).json()
       #print (get_data)
       channel_id = get_data ['channel'] ['id']
       
       field_1 = get_data ['feeds']
       #print (field_1)
       
       t = [ ]
       for x in field_1: 
              #print(x['field1'])
              t.append(x['field1'])
       print (t)
       
       data=urllib.request.urlopen(NEW_URL)

if __name__ == "__main__": 
       
       read_data_thingspeak()

#Reference: The code is based on "read data from thingspeak using python Raspberry pi or arduino", 2018, soumilshah1995
#                      Link : https://www.youtube.com/watch?v=whXaVYSXItQ
