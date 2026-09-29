import time
import board
import adafruit_dht
from w1thermsensor import W1ThermSensor 
from time import sleep
from gpiozero import LED
dhtDevice = adafruit_dht.DHT11(board.D18)
sensor = W1ThermSensor()
groen = LED(14)
rood = LED(8)
oranje = LED(7)
teller = 0
while True:
    try:
        sleep(1)
        teller = teller + 1
        temperature_c = float(dhtDevice.temperature) #DHT11
        temperature_in_celsius = sensor.get_temperature() #BS18D20
        sleep(1)

        if temperature_c - temperature_in_celsius < 1:
            groen.on()
            rood.off()
            oranje.off()
            print(f"{teller}   DHT11: {temperature_c: .1f} C / BS18D20: {temperature_in_celsius} C - Groene Led")
        elif temperature_c - temperature_in_celsius > 5:
            rood.on()
            groen.off()
            oranje.off()
            print(f"{teller}   DHT11: {temperature_c: .1f} C / BS18D20: {temperature_in_celsius} C - Rode Led")
        else:
            oranje.on()
            groen.off()
            rood.off()
            print(f"{teller}   DHT11: {temperature_c: .1f} C / BS18D20: {temperature_in_celsius} C - Oranje Led")


        time.sleep(1.0)
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(1.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
