import cPickle as Pickle
import codecs
'''
This file reads in the raw vocab tests from the local text version of the web PDF,
and converts to a python dictonay of questions and answers.  
'''

#read in the raw files
test_a = []
with open("Vocabulary Size Test: Version A.txt",'r') as fin:
	for line in fin.readlines():
		line = line.strip()
		if len(line)>0:
			test_a.append(line)
test_b = []
with open("Vocabulary Size Test: Version B.txt",'r') as fin:
	for line in fin.readlines():
		line = line.strip()
		if len(line)>0:
			test_b.append(line)
test_a_answers = []
with open("Vocabulary Size Test Version A answers.txt") as fin:
	for line in fin.readlines():
		line = line.strip()
		if len(line)>0:
			test_a_answers.append(line)
test_b_answers = []
with open("Vocabulary Size Test Version B answers.txt") as fin:
	for line in fin.readlines():
		line = line.strip()
		if len(line)>0:
			test_b_answers.append(line)

#clean the files:
clean_questions_a = {}
new_question = True
temp_answers = []
for line in test_a:
	if new_question:
		q_num = line[:line.index('.')]
		q_word = line[line.index(' ')+1:line.index(':')]
		q_phrase = line[line.index(':')+2:]
		#print q_num,q_word,q_phrase
		new_question = False
		continue
	this_answer = line[2:]
	temp_answers.append(this_answer)
	if len(temp_answers)==4:
		this_q = {}
		this_q['number'] = int(q_num)
		this_q['word'] = q_word
		this_q['phrase'] = q_phrase
		this_q['choices'] = temp_answers
		clean_questions_a[q_num] = this_q
		new_question = True
		temp_answers = []

clean_questions_b = {}
for line in test_b:
	if new_question:
		q_num = line[:line.index('.')]
		q_word = line[line.index(' ')+1:line.index(':')]
		q_phrase = line[line.index(':')+2:]
		#print q_num,q_word,q_phrase
		new_question = False
		continue
	this_answer = line[2:]
	temp_answers.append(this_answer)
	if len(temp_answers)==4:
		this_q = {}
		this_q['number'] = int(q_num)
		this_q['word'] = q_word
		this_q['phrase'] = q_phrase
		this_q['choices'] = temp_answers
		clean_questions_b[q_num] = this_q
		new_question = True
		temp_answers = []

clean_answers_a = {}
for line in test_a_answers:
	this_a = {}
	a_number = line[:line.index('.')]
	a_answer = line.split(" ")[-1]
	a_word = line.split(" ")[-2]
	this_a['number'] = int(a_number)
	this_a['answer'] = a_answer
	this_a['word'] = a_word
	clean_answers_a[a_number] = this_a

clean_answers_b = {}
for line in test_b_answers:
	this_a = {}
	a_number = line[:line.index('.')]
	a_answer = line.split(" ")[-1]
	a_word = line.split(" ")[-2]
	this_a['number'] = int(a_number)
	this_a['answer'] = a_answer
	this_a['word'] = a_word
	clean_answers_b[a_number] = this_a

#make the questions:
vocab_questions = {}
for q_num in clean_questions_a:
	this_vocab = {}
	this_vocab['word'] = clean_questions_a[q_num]['word']
	this_vocab['phrase'] = clean_questions_a[q_num]['phrase']
	this_vocab['choices'] = clean_questions_a[q_num]['choices']
	this_vocab['answer'] = clean_answers_a[q_num]['answer']
	vocab_questions[q_num] = this_vocab

for q_num in clean_questions_b:
	this_vocab = {}
	this_vocab['word'] = clean_questions_b[q_num]['word']
	this_vocab['phrase'] = clean_questions_b[q_num]['phrase']
	this_vocab['choices'] = clean_questions_b[q_num]['choices']
	this_vocab['answer'] = clean_answers_b[q_num]['answer']
	vocab_questions[q_num+'b'] = this_vocab

Pickle.dump(vocab_questions,open('vocab_questions.pickle','wb'))
print "Vocab questions created and pickled!"