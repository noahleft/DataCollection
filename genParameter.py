#!/usr/bin/env python
from sys import argv
from config import filepath,tableName,targetNum


feature=argv[1]
row_id =argv[2]

print(feature,row_id)

from sqlite3 import connect
conn=connect(filepath)
cursor=conn.cursor()

cursor.execute('SELECT '+','.join(list(map(lambda x: 'TARGET'+str(x),range(targetNum))))+' FROM '+tableName+' WHERE ID='+row_id)
targetList=cursor.fetchone()

print(targetList)

