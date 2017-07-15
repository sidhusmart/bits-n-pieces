import sys
import os
import subprocess

hdfsDirectory = "/sidharth/test1/" 
cat = subprocess.Popen(["hadoop", "fs", "-mkdir", hdfsDirectory], stdout=subprocess.PIPE)
cat.communicate()

localFile = "/home/hduser/Data/Aircel_Logs.txt"
cat = subprocess.Popen(["hadoop", "fs", "-put", localFile, hdfsDirectory], stdout=subprocess.PIPE)
cat.communicate()
