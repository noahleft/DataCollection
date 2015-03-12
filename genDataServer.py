#!/usr/bin/env python

from dataServer.dataServer import dataServer
from config import filepath,tableName,targetNum,featureNum

data=dataServer(tableName=tableName,targetNum=targetNum,featureNum=featureNum,filepath=filepath)
data.setup()


#data.createDataRow()
data.createCompleteDataRow()

