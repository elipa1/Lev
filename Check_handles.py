import os
import time
while True:
    n = os.popen("ls /proc/4413/fd | wc -l")
    handles =n.read()
    m=os.popen("top | grep nginx")
    mem=m.read()
    mem1=str(mem)
    print ("Number of handles is:", handles)
    print("Memory Usage is:", mem1)
    time.sleep(2)

from selenium import webdriver
