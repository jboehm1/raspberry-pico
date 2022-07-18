import utime #TODO : compare with "time"
import pico_tools

oled_display = pico_tools.InitOled()
sensor_temp = pico_tools.InitTempSensor()
led = pico_tools.InitLed()
servo = pico_tools.InitPwm()
#while True:
 #   pico_tools.MoveText(oled_display, "test", 0, 64, 0, 64)

def main():
    run = True
    while run:
        #pico_tools.DrawRect(oled_display, 20,20, 60, 20)
        #pico_tools.DrawFilledRect(oled_display, 20,20,60,20,0.9)
        for progress in range(100):
            pico_tools.DrawProgressBarDoted(oled_display, 20,20, 60, 30, progress/100, 3, 1, 2, 2)
            oled_display.show()
          
        temp = pico_tools.ReadTemp(sensor_temp)
        ratio = (temp - 16 )/4
        servo.duty_u16( int(ratio * 65535) )
        
        if temp > 12:
            led.value(1)
            pico_tools.MoveText(oled_display, "TEMP:{:2.2f}C".format(temp), 0, 64, 0, 64, 1)
            led.value(0)
            #pico_tools.DispOled(oled_display, "OVERTEMP: {:2.2f}C".format(temp), x=40, clean=True)
        else:
            pico_tools.DispOled(oled_display, "Temp:{:2.2f}C".format(temp), clean=True)
            led.value(0)
        utime.sleep(0.1)
        print(temp)

if __name__ == "__main__":
    main()