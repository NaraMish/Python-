#!/usr/bin/python3
#wifi hotspot enabler

import os
os.system('cls')
print('\n\n\n\n\n')
print('Nexus Wifi Hotspot Enabler')
print('(c)2021 Nexus Group.All right reserved.')
print()

cmd='0'
while cmd != '3' :
    print('1-Start Hotspot')
    print('2-Stop Hotspot')
    print('3-exit')
    cmd=input('Please Enter Your Choice(1,2,3): ')
    if cmd == '1':
        print('Starting Wifi hotspot....')
        os.system("netsh wlan set hostednetwork mode=alow ssid=Nexus key=12345678")
        os.system('netsh wlan start hostednetwork')
    elif cmd == '2':
        print('Stopping Wifi hotspot....')
        os.system('netsh wlan stop hostednetwork')
    elif cmd == '3':
        print('Exiting Program....')
        quit()

    else:
        print("Bad input! Please try again (Only 1,2,3)")
        os.system('pause')


