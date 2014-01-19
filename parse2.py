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




def traverseFiles(dataFileNames, threadNr):
    print "starting ", threadNr 
    t = Timer()
    t.click()
    i = 0
    for fileName in dataFileNames:
        print "\n thread ", threadNr, " doing ", fileName
        dataFile = open(config.get("data-dir") + fileName)
        for line in dataFile:
            i += 1
    t.click()
    print "read " , i, " lines in ", t.show()


T.click()

arg1 = dataFiles[0:5]
arg2 = dataFiles[5:10]
#threadNr = 1
#start_new_thread(traverseFiles, (arg1,threadNr,))
threadNr = 2
traverseFiles(arg2, threadNr)
T.click()
print "threaded reading in ", T.show()     




#print l.strip().split("\t")

# 1. reading  182.185.310  lines in  99.3188459873s
