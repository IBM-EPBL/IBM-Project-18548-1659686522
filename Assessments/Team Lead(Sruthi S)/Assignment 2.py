import random
import time
while True:
    temp= random.randint(0,150)
    print("Temperature= ",temp,'C')
    if (temp>=100):
        print("HIGH TEMPERATURE")
        print("Alarm ON")
    else:
        print("NORMAL TEMPERATURE")
    hum= random.randint(0,100)
    print("Humidity= ",hum,"%")
    time.sleep(3)
    print('\n')
