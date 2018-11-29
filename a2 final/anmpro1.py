import subprocess
import time
import json
import re
import MySQLdb

import MySQLdb

while(True):
  key = "bcf2edbe8c6d528bcf914759af63a253"

  proc = subprocess.Popen(["curl", "http://194.47.151.126:4000/emoncms/feed/list.json?userid=1&apikey="+key+""],   stdout=subprocess.PIPE)
  (out, err) = proc.communicate()
  a = []
  b = []
  c = []
  d = []
  e = []
  f = []
  g = []
  h = []
  k = []
  j=json.loads(out)


  for i in j:
   

    id1 = i['id']
    userid = i['userid']
    name = i['name']
    public = i['public']
    size = i['size']
    engine = i['engine']
    time1 = i['time']
    value = i['value']
    tag = i['tag']
    name1 = re.findall("tx\d_ws\d",name)
    if len(name1)==0:
        print id1,"|",userid,"|",name,"|",public,"|",size,"|",engine,"|",time1,"|",tag,"|",value

  time.sleep(2)  
      