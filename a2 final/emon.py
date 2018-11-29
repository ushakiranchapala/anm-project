import subprocess
import time
import json
import re
import MySQLdb

import MySQLdb

db=MySQLdb.connect(host="localhost",user="root",passwd="123456",db="first_db")
cur =db.cursor()


cur.execute("select address from emonpi where id like \"3\"")
for i in cur.fetchall():
    #print i[0]
    x=i[0]
    #print x
cur.close()
db.close()

proc = subprocess.Popen(["curl", x],   stdout=subprocess.PIPE)
(out, err) = proc.communicate()
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []
j=json.loads(out)


for i in j:
 

  id1 = i['id']
  userid = i['userid']
  name = i['name']
  public = i['public']
  size = i['size']
  engine = i['engine']
  time = i['time']
  value = i['value']
  #tag = i['tag']
 

  
  a.append(id1)
  b.append(userid)
  c.append(name)
  d.append(public)
  e.append(size)
  f.append(engine)
  g.append(time)
  h.append(value)
  #i.append(tag)
  #conn = MySQLdb.connect(host="localhost",user="root",passwd="adil",db="anm")
  #x = conn.cursor()
  for app1,app2,app3,app4,app5,app6,app7,app8 in zip(a,b,c,d,e,f,g,h,i):
     name1 = re.findall("tx\d_ws\d",app3) 
     
     if len(name1) ==0:
         print id
         print userid
         print name
         print public
         print size
         print engine
         print time
         print value
         #print tag
      #try:
       #x.execute("""INSERT INTO new(name,time,value) VALUES(%s,%s,%s)""",(app3,app7,app8))
       #onn.commit()
      #except:
       #conn.rollback()
       #conn.close()
print ('checkdb')
