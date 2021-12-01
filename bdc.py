#!/usr/bin/python3
import pbd
import time
a=1
def stayalive():
    time.sleep(5)
    pbd.connect()
while a ==1:
    time.sleep(30)
    try:
        stayalive()
    except:
        continue
