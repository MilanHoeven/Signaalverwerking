from gpiozero import LED,MCP3008
from time import sleep

potmeter = MCP3008(0)
led = LED(15)
while True:

    print(potmeter.value)
    led.on()
    sleep(2*potmeter.value)
    led.off()
    sleep(2*potmeter.value)