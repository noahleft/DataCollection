#!/usr/bin/env python


def createSQLtable(cursor,tableName='data',targetNum=4,featureNum=10):
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

