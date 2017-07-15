import sys
import os
import subprocess

hdfsFile = "/sidharth/test1/"
cat = subprocess.Popen(["hadoop", "fs", "-mkdir", hdfsFile], stdout=subprocess.PIPE)
cat.communicate()
