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

def DrawLine(oled_display, start_line_x=0, start_line_y=0, stop_line_x=50, stop_line_y=20, increment=1):
    for x in range(start_line_x, stop_line_x, increment):
        for y in range(start_line_y, stop_line_y, increment):
            oled_display.pixel(x, y, 1)
            
def DrawRect(oled_display, x, y, width, height):
    DrawLine(oled_display, x, y, x+width, y)
    DrawLine(oled_display, x, y, x, y+height)
    DrawLine(oled_display, x+width, y, x+width, y+height)
    DrawLine(oled_display, x, y+height, x+width, y+height)
    
#def DrawFilledRect():    
    
def ProgressBar(oled_display, progress=0.5, x=0, y=0, width=50, height=20):
    pass
    
    
    
    
    
def DispOled(oled_display, text, x=0, y=0, clean=True):
    if clean:
        oled_display.fill(0)
    oled_display.text(text, y, x, 1)

    #write15 = Write(oled_display, ubuntu_mono_15)
    #write20 = Write(oled_display, ubuntu_mono_20)

    #write20.text("OLED", 0, 0)
    #write15.text("Display", 0, 20)
    #oled.text("ElectroniClinic", 0, 40)
    oled_display.show()
    #utime.sleep(0.2)
 
def MoveText(oled_display, text, x_start=0, x_stop=128, y_start=0, y_stop=256, speed=1):
    print (max(x_stop-x_start, y_stop-y_start) )
    y_list=range(y_start, y_stop, speed)
    y_list_inv=range(y_stop, y_start, -speed)
    x_list = range(x_start, x_stop, 1)
    for ind, y in enumerate(y_list):
        DispOled(oled_display, text, y, x_list[ind])
        #print(y, x_list[ind])
    for ind, y in enumerate(y_list_inv ):
        DispOled(oled_display, text, y, x_list[-ind])
        #print(y, x_list[-ind])
#     for x in range(x_start, x_stop, 1): #range(start, end, step)
#         for y in range(y_start, y_stop, 1):
#             DispOled(oled_display, text, y, x)
#             print(x, y) 
#     for x in range(x_stop, x_start, -1): #range(start, end, step)
#         for y in range(y_stop, y_start, -1):
#             DispOled(oled_display, text, y, x)
            #print(x, y)
