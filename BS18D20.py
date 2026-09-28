from w1thermsensor import W1ThermSensor 
from time import sleep

sensor = W1ThermSensor()
while True:
    temperature_in_celsius = sensor.get_temperature()
    print(temperature_in_celsius)
    sleep(2)

