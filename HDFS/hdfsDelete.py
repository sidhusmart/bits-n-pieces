import sys
import os
import subprocess

hdfsFile = "/sidharth/test1/"
cat = subprocess.Popen(["hadoop", "fs", "-rmr", hdfsFile], stdout=subprocess.PIPE)
cat.communicate()
