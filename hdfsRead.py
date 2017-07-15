import sys
import os
import subprocess

hdfsFile = "/sidharth/test/bible.txt"
cat = subprocess.Popen(["hadoop", "fs", "-cat", hdfsFile], stdout=subprocess.PIPE)
for line in cat.stdout:
    print line
