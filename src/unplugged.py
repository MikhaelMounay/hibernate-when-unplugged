"""
import psutil
from plyer import notification
import time

def notifyme():
    battery = psutil.sensors_battery()
    is_plugged_in = battery.power_plugged
    # print(is_plugged_in)
    if (is_plugged_in == False):
        notification.notify(title="Charger is Plugged off",
                            message="Plug in the charger quickly",
                            app_icon="D:\\Mikha\\Plugged off Script\\plug_in.ico",
                            timeout=180,
                            )

while (True):
    
    notifyme()

    time.sleep(6)
    continue
"""

from psutil import sensors_battery
from plyer import notification
from time import sleep
from os import system

def notifyme():

    hibernate_timer = 15
    def send_notification(timer):
        noti_message = "The Laptop will HIBERNATE if the charger is not connected within " + str(timer) + " seconds"
        notification.notify(title="Charger is Plugged off",
                            message=noti_message,
                            app_icon="plug_in.ico",
                            )
    
    
    is_plugged_in_1 = sensors_battery().power_plugged
    # print(is_plugged_in)
    if (is_plugged_in_1 == False):
        for i in range(2):
            send_notification(hibernate_timer/(i+1))
            #print("loop no ", i)
            sleep(hibernate_timer/2)
            is_plugged_in_2 = sensors_battery().power_plugged
            if (is_plugged_in_2 == True):
                break
            elif(i == 1):
                system("shutdown -h")


while (True):
    
    notifyme()

    sleep(1)
