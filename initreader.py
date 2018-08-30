#A module to pass values to the mccurl/main script

def cfgread(filename):
	entrynum = 0 #Tracks number of entries in cfg
	entrylist = []
	authlist = []
	userlist = []
	idlist = []
	f = open(filename,"r")
	for line in f:
		if line[0] == "#":
			pass
		elif line[0] == ">":
			line = line.strip("\n")
			line = line.strip(">")
			entrylist.append(line)
			entrynum += 1
		elif line[0] != ">" or line[0] != "#":
			if line.find("user") != -1:
				line = line.lower()
				line = line.replace("user:","")
				line = line.strip(" ")
				line = line.strip("\n")
				userlist.append(line)
			if line.find("auth") != -1:
				line = line.lower()
				line = line.replace("auth:","")
				line = line.strip(" ")
				line = line.strip("\n")
				authlist.append(line)
			if line.find("listid") != -1:
				line = line.lower()
				line = line.replace("listid:","")
				line = line.strip(" ")
				line = line.strip("\n")
				idlist.append(line)
		else:
			pass
	entrydict = {}
	for i in range(0,entrynum):
		entrydict[entrylist[i]] = (userlist[i], authlist[i], idlist[i])
	return entrydict