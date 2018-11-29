import subprocess
import time
import json
import re
import MySQLdb
proc = subprocess.Popen(["curl", "http://194.47.151.126:4000/emoncms/feed/list.json?userid=1&apikey=bcf2edbe8c6d528bcf914759af63a253"],   stdout=subprocess.PIPE)
(out, err) = proc.communicate()
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
j=json.loads(out)
print out
