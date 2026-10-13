from gpiozero import LED,MCP3008
from time import sleep
digi = MCP3008(0)
import board
import adafruit_dht
dhtDevice = adafruit_dht.DHT11(board.D18)
import time
import csv
with open('eggs.csv', newline = '') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='/')
    for now in spamreader:
        print(', '.join(row))




while True:
    spanning = (digi.value/1) * 5.0
    temp = (spanning - 0.5)/0.01      
    sleep(1)
    print(temp)
    try:
        temperature_c = dhtDevice.temperature
        print(f"Temp: {temperature_c:.1f}")
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(3.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    
    time.sleep(3.0)
    


