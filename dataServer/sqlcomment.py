#!/usr/bin/env python


def createSQLtable(cursor,tableName='data',targetNum=6,featureNum=10):
  comment="""
  CREATE TABLE IF NOT EXISTS config(
  ID      INTEGER PRIMARY KEY AUTOINCREMENT,
  NAME    TEXT NOT NULL UNIQUE,
  TARGET  INTEGER NOT NULL,
  FEATURE INTEGER NOT NULL
  )"""
  cursor.execute(comment)
  comment="INSERT INTO config (NAME,TARGET,FEATURE) VALUES ("+",".join(list(map(lambda x:str(x),['"'+tableName+'"',targetNum,featureNum])))+");"
  cursor.execute(comment)
  comment="CREATE TABLE "+tableName+"(ID   INTEGER PRIMARY KEY AUTOINCREMENT,\n"+ \
  ",\n".join(list(map(lambda x:"TARGET"+str(x)+" REAL NOT NULL",range(targetNum))))+",\n"+ \
  ",\n".join(list(map(lambda x:"FEATURE"+str(x)+" REAL ",range(featureNum))))+")"
  cursor.execute(comment)

def createSQLdata(cursor,tableName='data',targetNum=6,targetList=[]):
  if len(targetList)==targetNum:
    comment="INSERT INTO "+tableName+" ("+",".join(list(map(lambda x:'target'+str(x),range(targetNum))))+") VALUES ("+ \
            ",".join(list(map(lambda x:str(x),targetList)))+");"
    cursor.execute(comment)

def selectSQLdata(cursor,tableName='data',targetNum=6,rowID=1):
  comment="SELECT "+",".join(list(map(lambda x:'target'+str(x),range(targetNum))))+" FROM "+tableName+" WHERE ID="+str(rowID)+";"
  cursor.execute(comment)
  return cursor.fetchone()
