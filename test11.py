#coding:utf8

import time
import subprocess
import os
wd = r"D:\搜狗高速下载\下载\TextDetection\examples"
files = os.listdir(wd)
for f in files:
    print "./Features textDetection %s%s %sout0%s 0" % (wd,f,wd,f)
    subprocess.call("./Features textDetection %s%s %sout0%s 0" % (wd,f,wd,f), shell=True)
    print "./Features textDetection %s%s %sout0%s 1" % (wd,f,wd,f)
    subprocess.call("./Features textDetection %s%s %sout1%s 1" % (wd,f,wd,f), shell=True)
    


time.sleep(10)


