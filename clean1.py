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
        print "\nthread ", threadNr, " cleaning ", fileName
        dataFile = open(config.get("data-dir") + fileName)
        resultFile = open(config.get("clean-dir") + "clean_" + fileName, "w")
        
        for line in dataFile:
            firstChar = line[0]
            
            # line is URL
            if firstChar == "U":
                resultFile.write(line)
                #print line[3].split("http://en.wikipedia.org/wiki/")[1]
                
            # line is a MENTION
            elif firstChar =="M":
                resultFile.write(line)
                
            # line is a TOKEN, exclude them.
            elif firstChar == "T":
                continue
                
            # line is a separator between two documents
            elif firstChar == "\n":
                resultFile.write(line)
            else: 
                print "ERROR: strange line: ", line
    
            
        resultFile.close()  
            
    t.click()
    print "thread ", threadNr, " done in ", t.show()



# 1. read the data into memory
############################################################
#argLeft = dataFiles[0:5]
argRight = dataFiles[5:10]
#argLeft = dataFiles
traverseFiles(argRight, threadNr)



#print l.strip().split("\t")

# 1. reading  182.185.310  lines in  99.3188459873s
