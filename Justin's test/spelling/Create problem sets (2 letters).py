import random, sys
import cPickle as Pickle

"""
This file uses the fullable.lst to make the two letter word questions.
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

fake_2_letter_words = ['gy', 'gg', 'ga', 'gj', 'gh', 'le', 'ty', 'lu', 'tj', 'yi', 'yh', 'yn', 'ya', 'yd', 'yy', 'ys', 'yr', 'yw', 'qj', 'eo', 'ej', 'ed', 'za', 'eb', 'ey', 'zy', 'eu', 'et', 'ew', 'ev', 'eq', 'ru', 'rd', 'rm', 'ri', 'wj', 'wi', 'js', 'jn', 'wt', 'ji', 'wp', 'jd', 'je', 'wh', 'ja', 'oj', 'og', 'wu', 'oa', 'oz', 'ot', 'co', 'xa', 'ce', 'xe', 'cy', 'xy', 'pu', 'py', 'pe', 'ir', 'hu', 'ux', 'ap', 'uu', 'mw', 'ui', 'uh', 'mr', 'ue', 'ud', 'uf', 'uc', 'ix', 'ab', 'ag', 'af', 'aj', 'iu', 'ao', 'ii', 'zt', 'ij', 'au', 'il', 'ia', 'ic', 'ni', 'du', 'fe', 'fo', 'sy', 'ke', 'kj', 'ki', 'su', 'sc', 'se']
'''
Create a bunch of problem sets.
These are groups of 1 real word, and a bunch of misspelled fake words.
The real word is listed first in each set.
'''
print "Creating problem sets..."
problem_sets = []
all_fake_words = set()
#for word_length in [3,7]:
for word in len_sets[2]:
	random_word = word.lower()
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
				if fake_word.upper() in all_words:
					pass#print "\nit's real!",fake_word
				else:
					if len(fake_word) != 2:
						pass#discard as too long or too short
					else:
						#print fake_word
						fake_words.add(fake_word.lower())
						all_fake_words.add(fake_word.lower())
			if set_match:break


	this_problem_set = [random_word]+list(fake_words)
	while len(this_problem_set)<4:
		this_problem_set.append(random.choice(fake_2_letter_words))
		this_problem_set = [this_problem_set[0]]+list(set(this_problem_set[1:]))
	#print this_problem_set#[:5]
	problem_sets.append(this_problem_set)
	
#print list(all_fake_words)
Pickle.dump(problem_sets,open("spelling_problem_2_words_sets.pickle",'wb'))
print "Done!  %s problem sets have been created and pickled."%(len(problem_sets))