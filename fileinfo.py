#!/usr/bin/python
import os,time
import zipfile
from datetime import datetime as d
import hashlib as hs
import ntpath
if not os.path.exists("/home/j1axs01/jc/targetdir"):
    os.makedirs("/home/j1axs01/jc/targetdir")
targetdir="/home/j1axs01/jc/targetdir"
zip_ref = zipfile.ZipFile("/home/j1axs01/jc/test1.zip", 'r')
zip_ref.extractall("/home/j1axs01/jc/targetdir")
zip_ref.close()
print("###############filename##############")
print(ntpath.basename("/home/j1axs01/jc/test.txt"))
print("###############extension###############")
print(os.path.splitext("/home/j1axs01/jc/test.txt")[1])
print("###############time in readable format ###############")
print(time.strftime('%D %H:%M:%S', time.gmtime(os.path.getmtime("/home/j1axs01/jc/test.txt"))))
print(time.strftime('%D %H:%M:%S', time.gmtime(os.path.getctime("/home/j1axs01/jc/test.txt"))))
print("##############################")
print(os.stat("test.txt"))
print(os.path.getmtime("/home/j1axs01/jc/test.txt"))
sha=hs.sha256("test.txt")
num_lines = sum(1 for line in open("test.txt"))
print("################row counts##############")
print(num_lines)
print("###############sha256###############")
print(sha.hexdigest())
