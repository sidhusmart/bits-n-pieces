import sys
import os
import subprocess

hdfsFile = "/sidharth/test/bible1.txt"
localFile = "/home/hduser/Code/outputFile.txt"
cat = subprocess.Popen(["hadoop", "fs", "-put", localFile, hdfsFile], stdout=subprocess.PIPE)
cat.communicate()
