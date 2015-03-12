#!/usr/bin/env python
from sys import argv
from config import filepath,tableName,targetNum
from extract import extractSpeed

feature=argv[1]
feature_id=int(feature[7:])
row_id =argv[2]

print(feature,row_id)

from sqlite3 import connect
conn=connect(filepath)
cursor=conn.cursor()

cursor.execute('SELECT '+','.join(list(map(lambda x: 'TARGET'+str(x),range(targetNum))))+' FROM '+tableName+' WHERE ID='+row_id)
targetList=cursor.fetchone()
print(feature_id,targetList)
conditionStrList=list(map(lambda x: 'TARGET'+str(x)+'='+str(targetList[x]),range(targetNum)))


speed=extractSpeed()
if int(feature_id/2)==4:
  pass
elif int(feature_id/2)==1 or int(feature_id/2)==0:
  conditionStrList=[conditionStrList[x] for x in [0,1,4,5]]
elif int(feature_id/2)==3 or int(feature_id/2)==2:
  conditionStrList=[conditionStrList[x] for x in [2,3,4,5]]

comment='UPDATE '+tableName+' SET '+feature+'='+str(speed)+' WHERE '+' AND '.join(conditionStrList)

print(comment)
cursor.execute(comment)

conn.commit()

