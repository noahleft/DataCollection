#!/usr/bin/env python

from sqlite3 import connect
from os.path import isfile
from sqlcomment import createSQLtable

class dataServer:
  def __init__(self,tableName='data',targetNum=6,featureNum=10,filepath='tmp.db'):
    self.tableName=tableName
    self.targetNum=targetNum
    self.featureNum=featureNum
    self.filepath=filepath
  def createService(self):
    if isfile(self.filepath):
      print('check file path plz')
    else:
      self.conn=connect(self.filepath)
      cursor=self.conn.cursor()
      createSQLtable(cursor,tableName=self.tableName,targetNum=self.targetNum,featureNum=self.featureNum)
      self.conn.commit()
  def setup(self):
    if isfile(self.filepath):
      self.conn=connect(self.filepath)
    else:
      self.createService()
  def getNumDataRow(self):
    if self.conn:
      cursor=self.conn.cursor()
      dataRows=cursor.execute('select count(*) from data').fetchone()[0]
      print('there are '+str(dataRows)+' data rows in the data table.')


