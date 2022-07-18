import utime #TODO : compare with "time"
import pico_tools
import time

oled_display = pico_tools.InitOled()
sensor_temp = pico_tools.InitTempSensor()
led = pico_tools.InitLed()
servo = pico_tools.InitPwm()


#while True:
 #   pico_tools.MoveText(oled_display, "test", 0, 64, 0, 64)

def main():
    run = True
    y_plot=[pico_tools.ReadTemp(sensor_temp)]
    while run:
        for k in range(100):
            oled_display.fill(0)

            pico_tools.CreateSine(oled_display, k*2/100)
            oled_display.show()

        utime.sleep(10)
        #pico_tools.DrawRect(oled_display, 20,20, 60, 20)
        #pico_tools.DrawFilledRect(oled_display, 20,20,60,20,0.9)
        #pico_tools.DrawFilledRect2(oled_display, 20,20,50,20)
        for k in range(200):
            temp = pico_tools.ReadTemp(sensor_temp)
            print(temp)
            pico_tools.CreateY_plot(y_plot, temp)
            oled_display.fill(0)
            pico_tools.DispPlot(oled_display, y_plot )
            oled_display.text( str(str(temp)+"C") , 30,30)
            oled_display.show()
        
        utime.sleep(5)
        start = time.ticks_ms()
        for progress in range(101):
            pico_tools.DrawProgressBar2(oled_display, 20,20, 60, 30, progress/100)
            oled_display.text(" {:2.0f}%".format(progress), 80, 50, 1)
            
            oled_display.show()
            oled_display.fill(0)

        print("first loop ", time.ticks_ms() - start )
        
        utime.sleep(5)
        oled_display.fill(0)
        
        start = time.ticks_ms()
        for progress in range(101):
            pico_tools.DrawProgressBar(oled_display, 20,20, 60, 30, progress/100)
            oled_display.text(" {:2.0f}%".format(progress), 80, 50, 1)

            oled_display.show()
            oled_display.fill(0)

        print("second loop ", time.ticks_ms() - start )

        utime.sleep(5)
        
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