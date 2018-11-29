import MySQLdb

db=MySQLdb.connect(host="localhost",user="root",passwd="123456",db="first_db")
cur =db.cursor()
cur.execute("show tables")
for i in cur.fetchall():
    print i[0]

cur.execute("select address from emonpi where id like \"1\"")
for i in cur.fetchall():
    #print i[0]
    x=i[0]
    print x
cur.close()
db.close()
