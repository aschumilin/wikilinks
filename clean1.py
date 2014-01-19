"""
read wikilinks dataset
1. remove token entries
"""
import json, os
from Timer import Timer
from thread import start_new_thread



T = Timer()

config = json.load(open("config")) # dictionary of settings

dataFiles = os.listdir(config.get("data-dir"))


data= []
threadNr = 1

def traverseFiles(dataFileNames, threadNr):
    print "starting ", threadNr 
    t = Timer()
    t.click()
    for fileName in dataFileNames:
        print "\n thread ", threadNr, " doing ", fileName
        dataFile = open(config.get("data-dir") + fileName)
        for line in dataFile:
            data.append(line)
    t.click()
    print "thread ", threadNr, " done in ", t.show()


T.click()



traverseFiles(dataFiles[0:5],threadNr)
T.click()
print "thread 1 - reading done in ", T.show()     




#print l.strip().split("\t")

# 1. reading  182.185.310  lines in  99.3188459873s
