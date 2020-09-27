import httplib
import urllib
import time
from random import randint
key = "BTO7X06U644MHJ6D"  # Put your API Key here
def thermometer():
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
        temp = randint(10, 100)
        params = urllib.urlencode({'field1': temp, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print temp
            print response.status, response.reason
            data = response.read()
            conn.close()
        except:
            print "connection failed"
        break
if __name__ == "__main__":
        while True:
                thermometer()
                
#Reference: The code is based on "How to Send Data to ThingSpeak Cloud using Raspberry Pi", 2019, ioTDesignPro
#                      Link : https://iotdesignpro.com/projects/how-to-send-data-to-thingspeak-cloud-using-raspberry-pi
