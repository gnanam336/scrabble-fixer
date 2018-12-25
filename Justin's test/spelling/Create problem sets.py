import random
import cPickle as Pickle

"""
This file uses the fullable.lst and thousand_common.lst and picks 30 words from each.
It generates fake, misspelled words for each correct word, the collection is a problem set.
NOTE:  the first word in each set is the correct word.
A dictionary containing the problem sets is pickled for further use.
"""

print "Loading and sorting resources..."
##load all legal scrable words and the 1000 most common
all_words = []
with open("fullable.lst",'r') as fin:
	for line in fin.readlines():
		line = line.strip()
		if len(line) == 0:continue
		all_words.append(line)

thosand_words = []
with open("thousand_common.lst",'r') as fin:
	for line in fin.readlines():
		line = line.strip()
		if len(line) == 0:continue
		thosand_words.append(line)

##load all interchangable letters
letter_mixer = Pickle.load(open("matching_letters.pickle",'rb'))


#sort all words and the thousand words into length sets
len_sets = {}
all_words.sort(key = len)

for word in all_words:
	this_len = len(word)
	if this_len in len_sets:
		len_sets[this_len].append(word)
	else:
		len_sets[this_len] = [word]

len_sets_thousand = {}
thosand_words.sort(key = len)

for word in thosand_words:
	this_len = len(word)
	if this_len in len_sets_thousand:
		len_sets_thousand[this_len].append(word)
	else:
		len_sets_thousand[this_len] = [word]

'''
Create a bunch of problem sets.
These are groups of 1 real word, and a bunch of misspelled fake words.
The real word is listed first in each set.
'''
print "Creating problem sets..."
problem_sets = {}
for word_length in [3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,8,8,8,8,9,10]:
#for word_length in [3,7]:
	for d,diff in [(len_sets,'hard'),(len_sets_thousand,'easy')]:
		#pick a random word of the correct length
		random_word = random.choice(d[word_length]).lower()
		while not random_word.isalnum():#if we got one with non letters, try again.
			random_word = random.choice(d[word_length]).lower()
		fake_words = set()
		#print random_word
		for letter_set in letter_mixer:
			set_match = False
			for l in letter_set:
				if l in random_word:
					set_match = True
					temp_set = letter_set[:]
					temp_set.remove(l)
					new_l = random.choice(temp_set)
					fake_word = random_word.replace(l,new_l)
					if fake_word.upper() in all_words or len(fake_word)<3:
						pass#print "\nit's real!",fake_word
					else:
						fake_words.add(fake_word.lower())
				if set_match:break

		if not diff in problem_sets:problem_sets[diff]=[]
		this_problem_set = [random_word]+list(fake_words)
		if len(this_problem_set)<4:
			print this_problem_set
			continue
		#print diff,this_problem_set[:5]
		problem_sets[diff].append(this_problem_set)

Pickle.dump(problem_sets,open("spelling_problem_sets.pickle",'wb'))
print "Done!  Problem sets has been created and pickled. %s questions created."%(len(problem_sets["easy"])*2)
