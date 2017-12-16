import sys
import os
import subprocess

hdfsFile = "/sidharth/test/bible.txt"
outputFile = "/home/hduser/Code/outputFile.txt"
outputBuffer = open(outputFile, 'w')
cat = subprocess.Popen(["hadoop", "fs", "-cat", hdfsFile], stdout=subprocess.PIPE)
for line in cat.stdout:
	outputBuffer.write(line)
outputBuffer.close()
