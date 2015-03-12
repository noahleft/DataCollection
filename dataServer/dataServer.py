#!/usr/bin/env python

from sqlite3 import connect
from os.path import isfile

class dataServer:
  def __init__(self):
    pass
  def createService(self,filepath):
    if isfile(filepath):
      print 'check file path plz'
    else:
      self.conn=connect(filepath)
  def setup(self,filepath):
    if isfile(filepath):
      self.conn=connect(filepath)
    else:
      self.createService(filepath)



