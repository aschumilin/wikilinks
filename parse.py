'''
read the cleaned files to dicitonaries
Number of Mentions: 40,323,863
Number of Entities:     2,933,659
Number of pages:      10,893,248
'''
import json, os, sys, csv
from Timer import Timer

T = Timer()
config = json.load(open("config")) # dictionary of settings
dataFiles = os.listdir(config.get("clean-dir"))


# 1. read the data into memory
############################################################

data = []
T.click()

for fileName in dataFiles:
    dataFile = open(config.get("clean-dir") + fileName)
    print "processing ", fileName
    for line in dataFile:
        data.append(line)
        
T.click()


size = sys.getsizeof(data) / 1000000.0
print "data array size: ", str(size), "MB"
print "filling data array done in ", T.show()





"""
>
>
URL     ftp://212.18.29.48/ftp/pub/allnet/nas/all60600/ALL60600_UM_EN.pdf
MENTION NetBIOS 186757  http://en.wikipedia.org/wiki/NetBIOS
>
>
URL     ftp://38.107.129.5/Training/Traininga.pdf
MENTION Microsoft       80679   http://en.wikipedia.org/wiki/Microsoft
>
>
"""

# 2. put data in dictionaries
############################################################

T.click()
docDict = dict()
entDict = dict()
phraseDict = dict()
sparseTensor = []

docCount = 0
entCount = 0
phraseCount = 0

i=0
j = 1
numLines = len(data)
while i < numLines:


	# line is URL
	if data[i][0] == "U":
		
		# 1. read document name (address)

		docName = data[i].split("\t")[1]

		docIndex = docDict.get(docName)
		if docIndex == None:
			# add unknown document 
			docDict.update({docName : docCount})
			docIndex = docCount
			docCount += 1 
		


		i += 1

		# TEST
		if not data[i][0]=="M":
			print "ERROR: line after URL is not a MENTION: ", data[i]
			print "exiting loop..."
			break
		


		# 2. parse the following MENTION lines

		while data[i][0]=="M":
			tokens = data[i].split("\t")
			entity = tokens[3].split("/")[-1]
			phrase = tokens[1]
			
			# 2.1. search the dictionaries for the entity and phrase
			entIndex = entDict.get(entity)			
			if  entIndex == None:
				# add unknown entity
				entDict.update({entity : entCount})
				entIndex = entCount 
				entCount += 1

			phraseIndex = phraseDict.get(phrase)
			if phraseIndex == None:
				# add unknown phrase
				phraseDict.update({phrase : phraseCount})
				phraseIndex = phraseCount
				phraseCount += 1
				
			# 2.2. append entry to the sprase tensor representation
			sparseTensor.append([docIndex, entIndex, phraseIndex])	
				
				
			# !!!! increment line count
			i += 1

		
	# line is a separator between two documents
	elif data[i][0] == "\n":
		i += 1
		continue
	else: 
		print "ERROR: strange line: ", line
	
	if (i % 100000) == 0:
		print str(j*100000)
		j += 1
		
		
T.click()

print "building sparse tensor representation done in ", T.show()



# 3. write result files to disk
############################################################


T.click()
resultEntDictFile = config.get("result-dir") + "wikilinks_ent_dict.json"
resultPhraseDictFile = config.get("result-dir") + "wikilinks_phrase_dict.json"
resultDocDictFile = config.get("result-dir") + "wikilinks_doc_dict.json"
resultTensorFile = config.get("result-dir") + "wikilinks_sparse_tensor_repr.csv"

saveDicts = open(resultEntDictFile, "w")
saveDicts.write(json.dumps(entDict))
saveDicts.close()

saveDicts = open(resultPhraseDictFile, "w")
saveDicts.write(json.dumps(phraseDict))
saveDicts.close()

saveDicts = open(resultDocDictFile, "w")
saveDicts.write(json.dumps(docDict))
saveDicts.close()


tensorFile = open(resultTensorFile, "wb")
fileWriter = csv.writer(tensorFile, delimiter=';', quoting=csv.QUOTE_NONE)
for row in sparseTensor:
	fileWriter.writerow(row)
tensorFile.close()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

T.click()

print "saving result files done in ", T.show()


# 4. print some stats
############################################################

print "=== SUMMARY ==="
print "found ", len(sparseTensor), " entity mentions in ", len(docDict), " articles"
print " number of distinct entities: ", len(entDict)
print " referred to by ", len(phraseDict), " distinct phrases"





