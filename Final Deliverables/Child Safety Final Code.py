import time
import sys
import ibmiotf.application
import ibmiotf.device
import random

#Provide your IBM Watson Device Credentials
organization = "zyb99x"
deviceType = "IBM"
deviceId = "08"
authMethod = "token"
authToken = "12345678"

# Initialize GPIO
def myCommandCallback(cmd):
    print("Command received: %s" % cmd.data['command'])
    status=cmd.data['command']
    if status=="Buttonpressed":
                print("Child in danger")
    else:
                print("please send proper command")

try:
    deviceOptions = {"org": organization, "type": deviceType, "id":deviceId,"auth-method":authMethod, "auth-token":authToken}
    deviceCli=ibmiotf.device.Client(deviceOptions)
#....................

except Exception as e:
                     print("Caught exception connecting device: %s" % str(e))
                     sys.exit()

#connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
                     #get sensor data from DHT11
                     childtemp=random.uniform(96.70,99.30)
                     childtemp=round(childtemp,2)
                     childhb=random.randint(55,85)
                     data={'childtemp': childtemp, 'childhb': childhb}
                     #print data
                     def myOnPublishCallback():
                         print ("Published Child Temperature =%s F" % childtemp, "Heartbeat=%s BPM" %childhb,"to IBM Watson")
                         
                     success=deviceCli.publishEvent("IOTSensor","json",data, qos=0, on_publish=myOnPublishCallback)
                     if not success:
                         print("Not connected to IOTF")
                     time.sleep(10)

                     deviceCli.commandCallback=myCommandCallback

#disconnect the device and application from the cloud
deviceCli.disconnect()
                     
