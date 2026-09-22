from gpiozero import Button,LED
from signal import pause
teller = 0

led = LED(17)
knop = Button(14)

if knop == HIGH:
    teller = teller+1
elif teller == 1:
    led.on()
else:
    led.off()


