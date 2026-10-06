from gpiozero import LED,MCP3008
from time import sleep
led1 = LED(16)
led2 = LED(20)
led3 = LED(21)
led4 = LED(13)
led5 = LED(19)
led6 = LED(26)
digi = MCP3008(0)

while True:
    spanning = (digi.value/1) * 3.3
    temp = (spanning - 0.5)/0.01
    sleep(1)
    print(temp)
    if temp <= 5:
        led1.on()
        led4.off()
        led5.off()
        led6.off()
        led3.off()
        led2.off()
    elif temp >5 and temp <= 10:
        led2.on()
        led1.on()
        led4.off()
        led5.off()
        led6.off()
        led3.off()
    elif temp >10 and temp <=15:
        led3.on()
        led2.on()
        led1.on()
        led4.off()
        led5.off()
        led6.off()
    elif temp >15 and temp <= 20:
        led4.on()
        led3.on()
        led2.on()
        led1.on()
        led6.off()
        led5.off()
    elif temp >20 and temp <= 25:
        led5.on()
        led4.on()
        led3.on()
        led2.on()
        led1.on()
        led6.off()
    elif temp >25:
        led6.on()
        led5.on()
        led4.on()
        led3.on()
        led2.on()
        led1.on()