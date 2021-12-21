
import wiotp.sdk.device 
import os
import time
import datetime 
import random 

myConfig = {
    "identity": {
        "orgId": "e9psgv",
        "typeId": "RIFT",
        "deviceId": "2001"
    },
    "auth": {
        "token": "12345678"
    }
}

def myCommandCallback(cmd):
    print("Message recieved from IBM IoT Platform: %s" % cmd.data)
    m=cmd.data['command']
    if (m == "lighton"):
                print("Light is Switched ON")
    elif (m== "lightoff"):
                print("Light is Switched OFF")
    elif (m== "fanoff"):
                print("Fan is Switched OFF")
    elif (m== "fanon"):
                print("Fan is Switched OFF")
    print(" ")
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temp=random.randint(-20,125)
    hum=random.randint(0,100)
    myData={'temperature':temp, 'humidity': hum}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0 , onPublish=None)
    print("Published Data Successfully: %s",myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()

