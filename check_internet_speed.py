# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:52:19 2024

@author: brian
"""
import speedtest
import time
import os


# This is to keep track of starting monitoring time.
start = time.time()
# If the data file exists, delete, and start from the beginning. If there is none, pass.
try:
    os.remove('internet_speed.txt')
except OSError:
    pass


def internet_speed():
    speed_test = speedtest.Speedtest()
    download_speed = speed_test.download() / 1000000
    upload_speed = speed_test.upload() / 1000000
    end = time.time()
    sec = end - start
    print("Your Download speed is", download_speed)
    print("Your Upload speed is", upload_speed)
    print("Time spent (s):", sec)
    with open('internet_speed.txt','a') as f:
        f.write(str(sec) + ',' + str(download_speed) + ',' + str(upload_speed) + '\n')

if __name__ == '__main__':
    on =True
    while on == True:
        try: 
            internet_speed()
        except KeyboardInterrupt:
            on = False
            break
            print('Internet speed check interrupted!')