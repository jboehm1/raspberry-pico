import utime #TODO : compare with "time"
import pico_tools


oled_display = pico_tools.InitOled()
sensor_temp = pico_tools.InitTempSensor()
led = pico_tools.InitLed()
servo = pico_tools.InitPwm()

while True:
    
    
    temp = pico_tools.ReadTemp(sensor_temp)
    ratio = (temp - 16 )/4
    print(ratio)
    servo.duty_u16( int(ratio * 65535) )

    
    if temp > 12:
        led.value(1)
        pico_tools.DispOled(oled_display, "OVERTEMP: {:2.2f}C".format(temp), x=40, clean=True)

    else:
        pico_tools.DispOled(oled_display, "Temp:{:2.2f}C".format(temp), clean=True)
        led.value(0)
    utime.sleep(0.1)
    print(temp)