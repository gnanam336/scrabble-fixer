import re
import cPickle as Pickle
list_started = False
with open("replacement letters website.txt") as fin:
	current_list = []
	all_lists = []
	for line in fin.readlines():
		line = line.strip()
		if line == "<li>":
			if list_started:
				print "double list error!"
			list_started = True
			current_list = []
			continue
		if line == "</li>":
			if not list_started:
				print "double list error!"
			list_started = False
			if len(current_list)>0:
				all_lists.append(current_list)
			continue
		#print line
		sims = list(set(re.findall(r'<strong>(.+?)</strong>',line)))
		for x in ['&ntilde;','&eacute;','ou&rsquo;re','ey&rsquo;re']:
			if x in sims:
				sims.remove(x)
		if " city" in sims:
			sims.remove(" city")
			sims.append("ci")
		if "hl." in sims:
			sims.remove("hl.")
			sims.append("hl")
		if "arre." in sims:
			sims.remove("arre.")
			sims.append("arre")
		
		current_list = sims
		
Pickle.dump(all_lists,open("matching_letters.pickle",'wb'))
for a in all_lists:
	print a
