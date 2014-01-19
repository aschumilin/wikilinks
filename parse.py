'''
read the cleaned files to dicitonaries
'''
import json, os, sys
from Timer import Timer



T = Timer()

config = json.load(open("config")) # dictionary of settings

dataFiles = os.listdir(config.get("clean-dir"))

data = []
T.click()
lineCount = 0
for fileName in dataFiles:
    dataFile = open(config.get("clean-dir") + fileName)
    print "processing ", fileName
    for line in dataFile:
        lineCount += 1
        if lineCount%100000 == 0:
            print ".", 
        data.append(line)
        
T.click()
print "data size: ", sys.getsizeof(data)
print "processing done in ", T.show()