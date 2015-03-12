#!/usr/bin/env python

from sqlite3 import connect
from os.path import isfile
from sqlcomment import createSQLtable

class dataServer:
  def __init__(self):
    pass
  def createService(self,filepath):
    if isfile(filepath):
      print 'check file path plz'
    else:
      self.conn=connect(filepath)
      cursor=self.conn.cursor()
      createSQLtable(cursor)
      self.conn.commit()
  def setup(self,filepath):
    if isfile(filepath):
      self.conn=connect(filepath)
    else:
      self.createService(filepath)
  def getNumDataRow(self):
    if self.conn:
      cursor=self.conn.cursor()
      dataRows=cursor.execute('select count(*) from data').fetchone()[0]
      print('there are '+str(dataRows)+' data rows in the data table.')


