"""
read wikilinks dataset
1. remove token entries
"""
import json, os, sys
from Timer import Timer
#from thread import start_new_thread





config = json.load(open("config")) # dictionary of settings

dataFiles = os.listdir(config.get("data-dir"))

T = Timer()
data = []
threadNr = 2

def traverseFiles(dataFileNames, threadNr):
    print "starting ", threadNr 
    t = Timer()
    t.click()
    for fileName in dataFileNames:
        print "\nthread ", threadNr, " doing ", fileName
        dataFile = open(config.get("data-dir") + fileName)
        for line in dataFile:
            #data.append(line.strip().split("\t"))
            data.append(line)
            
        data.append("+ new file")
    t.click()
    print "thread ", threadNr, " done in ", t.show()



# 1. read the data into memory
############################################################
#argLeft = dataFiles[0:5]
#argRight = dataFiles[5:10]
argLeft = dataFiles
traverseFiles(argLeft, threadNr)


# 2. clean and save the data
############################################################
T.click()

fileNumber = 0
resultFile = open(config.get("clean-dir") + "wikilinks-cleaned-" + str(fileNumber), "w")

for line in data:
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
    
    # line is file separator. switch files here
    elif firstChar == "+":
        resultFile.close()
        fileNumber += 1
        resultFile = open(config.get("clean-dir") + "wikilinks-cleaned-" + str(fileNumber), "w")

        
    # line is a separator between two documents
    elif firstChar == "\n":
        resultFile.write(line)
    else: 
        print "ERROR: strange line: ", line

        
resultFile.close()      
T.click()
   

print T.show()

"""
docDict = dict()
entDict = dict()
phraseDict = dict()

docCount = 0
entCount = 0
phraseCount = 0


T.click()

for line in data:
    if line[0] == "MENTION":print line[3].split("http://en.wikipedia.org/wiki/")[1]
T.click()
   

print T.show()


"""

# 1. reading  182.185.310  lines in  99.3188459873s
