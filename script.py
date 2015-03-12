#!/usr/bin/env python

from dataServer.dataServer import dataServer

data=dataServer(tableName='data',targetNum=6,featureNum=10,filepath='tmp.db')
data.setup()


#data.createDataRow()
data.createCompleteDataRow()

