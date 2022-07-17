from machine import Pin, I2C, ADC, PWM
from ssd1306 import SSD1306_I2C
import utime
from oled import Write, GFX, SSD1306_I2C
from oled.fonts import ubuntu_mono_15, ubuntu_mono_20

#servo.freq(50)
def InitPwm(pin=0):
    return PWM(Pin(0))

def InitTempSensor():
    return ADC(4)

def InitLed(pin=25):
    return Pin(pin, Pin.OUT)

def ReadTemp(SENSOR_TEMP):
    reading = SENSOR_TEMP.read_u16() * 3.3/65535
    temp = round(27 - (reading - 0.706) / 0.001721, 2)
    return temp

def InitOled():
    WIDTH =128
    HEIGHT= 64
    i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)
    return SSD1306_I2C(WIDTH,HEIGHT,i2c)

def DispOled(oled_display, text, x=0, y=0, clean=True):
    if clean:
        oled_display.fill(0)
    oled_display.text(text, y, x, 1)

    write15 = Write(oled_display, ubuntu_mono_15)
    write20 = Write(oled_display, ubuntu_mono_20)

    write20.text("OLED", 0, 0)
    write15.text("Display", 0, 20)
    #oled.text("ElectroniClinic", 0, 40)
    oled_display.show()
    utime.sleep(0.2)
 
    
