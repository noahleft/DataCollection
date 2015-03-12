#!/usr/bin/env python

from sqlite3 import connect
from os.path import isfile
from sqlcomment import createSQLtable,createSQLdata,selectSQLdata
from random import randint

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
  def getNumDataRow(self,detail=False):
    if self.conn:
      cursor=self.conn.cursor()
      dataRows=cursor.execute('select count(*) from data').fetchone()[0]
      if detail==True:
        print('there are '+str(dataRows)+' data rows in the data table.')
      return dataRows
  def createDataRow(self,numRow=100,stepList=[(0.1,-3,3)]*4+[(0.02,-12,12),(1,-1,1)]):
    if self.conn:
      cursor=self.conn.cursor()
      for idx in range(numRow):
        createSQLdata(cursor,tableName=self.tableName,targetNum=self.targetNum,targetList=self.genRandomTargetList(stepList))
      self.conn.commit()
      self.getNumDataRow(detail=True)
  def selectDataRow(self,rowID=1):
    if self.conn:
      cursor=self.conn.cursor()
      return selectSQLdata(cursor,rowID=rowID)
  def genRandomTargetList(self,stepList):
    trum=lambda x: '%.3f' %x
    targetList=list(map(lambda x: float(trum(x[0]*randint(x[1],x[2]))),stepList))
    return targetList
  def analyze(self):
    distribution=[{} for x in range(self.targetNum)]
    for idx in range(1,int(self.getNumDataRow())+1):
      data=self.selectDataRow(rowID=idx)
      for idx2 in range(self.targetNum):
        if data[idx2] in distribution[idx2]:
          distribution[idx2][data[idx2]]+=1
        else:
          distribution[idx2][data[idx2]]=1
    return distribution
  def createCompleteDataRow(self,stepList=[(0.1,-3,3)]*4+[(0.02,-12,12),(1,-1,1)]):
    if self.conn:
      cursor=self.conn.cursor()
      for idx in range(75):
        targetListList=self.genSeededTargetList(idx,stepList)
        for targetList in targetListList:
          createSQLdata(cursor,tableName=self.tableName,targetNum=self.targetNum,targetList=targetList)
      self.conn.commit()
      self.getNumDataRow(detail=True)
  def genSeededTargetList(self,seed,stepList):
    Vt1=[]
    Vt2=[]
    while len(Vt1)<9:
      tmp=self.genRandomTargetList(stepList[:2])
      if not tmp in Vt1:
        Vt1.append(tmp)
    while len(Vt2)<9:
      tmp=self.genRandomTargetList(stepList[2:4])
      if not tmp in Vt2:
        Vt2.append(tmp)
    consT=[((seed%25)-12)*0.02,(seed/25)-1]
    targetListList=[x+y+consT for x in Vt1 for y in Vt2]
    return targetListList




