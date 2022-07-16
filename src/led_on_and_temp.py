import machine
from machine import ADC
import utime #TODO : compare with "time"

led = machine.Pin(25, machine.Pin.OUT)
SENSOR_TEMP = ADC(4)
CONVERSION_FACTOR= 3.3/65535

while True:
    reading = SENSOR_TEMP.read_u16() * CONVERSION_FACTOR
    temp = round(27 - (reading - 0.706) / 0.001721, 2)
    print(temp)
    led.value(1)
    utime.sleep(.01)
    led.value(0)
    utime.sleep(.1)