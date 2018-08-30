import requests
import json
from initreader import *


url = "https://us1.api.mailchimp.com/3.0/"
initfile = "init.txt"

listdict = cfgread(initfile)

for key in listdict:
	x = requests.get(url + "lists/" + listdict[key][2] + "/members", \
	auth=(listdict[key][0],listdict[key][1]))
	f = open(key + ".csv","w+")
	print("id,lastname,email,client,avg_open,avg_click",file=f)
	x = x.text
	x = json.loads(x)
	try:
		for i in range(0,len(x["members"])):
			memid = x["members"][i]["id"]
			print(memid + "," + \
				x["members"][i]["merge_fields"]["LNAME"] + r"," + \
				x["members"][i]["email_address"] + r"," + \
				x["members"][i]["email_client"] + r"," + \
				str(x["members"][i]["stats"]["avg_open_rate"]) + r"," + \
				str(x["members"][i]["stats"]["avg_click_rate"]),file=f)
		print("\"" + key + "\" list completed.")
	except KeyError:
		print("Request for \"" + key + "\" not fulfilled - check auth in init.txt.")
		
	f.flush()
	f.close()