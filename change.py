import json


paths = ["./results/wikilinks_ent_dict.json", "./results/wikilinks_doc_dict.json", "./results/wikilinks_phrase_dict.json"]


for path in paths:
	dic = json.load(open(path, "r"))
	changed = dict()
	
	for item in dic:
		changed.update({dic.get(item) : item})
		
	if not (len(dic) == len(changed)):
		print "ERROR: dict length mismatch: ", str(len(dic)) , " != ", str(len(changed))
		print "in ", path
	print "done: ", path	
	f = open (path, "w")
	f.write(json.dumps(changed))
	f.close()
	print "saved: ", path
		
		
		
"""
10888931;641063;1169029
10888931;892563;1828118
10888931;345283;100838
10888931;959314;1180067
10888932;1656739;437405
10888933;1294398;1828129
10888933;686028;852830
10888933;1348711;1828130
10888933;16188;17009
10888933;1348712;1828131
"""		
