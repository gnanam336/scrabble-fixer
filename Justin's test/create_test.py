'''
This file used the spelling and vocab pickles to create a JS resource file!

Output is in key/value JS dict form.  These dicts will be created:
easy_spelling (from 1000 most common words)
hard_spelling (from all words)
two_spelling  (from two letter words)
grammer       (from grammer tests)

Every question will have this form:
title:  <Choose the correct spelling:> or <Word: example sentance>
0:  <choice 1>
1:  <choice 2>
2:  <choice 3>
3:  <choice 4>
answer: <0,1,2, or 3>
value: <a score from 5 to 15.  5 for easy spelling, 10 for spelling, 10 for vocab, 20 for 2 letter spelling>
'''
import cPickle as Pickle
import random

spelling_questions = Pickle.load(open("final pickles/spelling_problem_sets.pickle",'rb'))
spelling_questions_2words = Pickle.load(open("final pickles/spelling_problem_2_words_sets.pickle",'rb'))
vocab_questions = Pickle.load(open("final pickles/vocab_questions.pickle",'rb'))



#create the 2 letter spelling questions
final_2_letter_questions = []
for x in spelling_questions_2words:
	#print x
	this_question = {}
	this_question["title"] = "Choose the correct spelling:"
	this_correct_answer = x[0]
	
	#select all the wrong answers
	this_wrong_answers = x[1:]
	#mix them up so that we can randomly pick three
	random.shuffle(this_wrong_answers)
	#grab the first three, which is the same as selecting three random wrong ones
	this_wrong_answers = this_wrong_answers[:3]
	#add back in the correct answer
	this_wrong_answers.append(this_correct_answer)
	this_answers = this_wrong_answers
	#mix in the correct answer
	random.shuffle(this_answers)
	this_index_of_correct = this_answers.index(this_correct_answer)
	#print this_answers,this_index_of_correct
	
	this_question["0"] = this_answers[0]
	this_question["1"] = this_answers[1]
	this_question["2"] = this_answers[2]
	this_question["3"] = this_answers[3]
	this_question["answer"] = this_index_of_correct
	this_question["value"] = 20
	#print this_question
	final_2_letter_questions.append(this_question)

#create the easy spelling questions
final_spelling_easy_questions = []
for x in spelling_questions["easy"]:
	#print x
	this_question = {}
	this_question["title"] = "Choose the correct spelling:"
	this_correct_answer = x[0]
	
	#select all the wrong answers
	this_wrong_answers = x[1:]
	#mix them up so that we can randomly pick three
	random.shuffle(this_wrong_answers)
	#grab the first three, which is the same as selecting three random wrong ones
	this_wrong_answers = this_wrong_answers[:3]
	#add back in the correct answer
	this_wrong_answers.append(this_correct_answer)
	this_answers = this_wrong_answers
	#mix in the correct answer
	random.shuffle(this_answers)
	this_index_of_correct = this_answers.index(this_correct_answer)
	#print this_answers,this_index_of_correct
	
	this_question["0"] = this_answers[0]
	this_question["1"] = this_answers[1]
	this_question["2"] = this_answers[2]
	this_question["3"] = this_answers[3]
	this_question["answer"] = this_index_of_correct
	this_question["value"] = 5
	#print this_question
	final_spelling_easy_questions.append(this_question)

	#print this_question
	#break

#create the hard spelling questions
final_spelling_hard_questions = []
for x in spelling_questions["hard"]:
	#print x
	this_question = {}
	this_question["title"] = "Choose the correct spelling:"
	this_correct_answer = x[0]
	
	#select all the wrong answers
	this_wrong_answers = x[1:]
	#mix them up so that we can randomly pick three
	random.shuffle(this_wrong_answers)
	#grab the first three, which is the same as selecting three random wrong ones
	this_wrong_answers = this_wrong_answers[:3]
	#add back in the correct answer
	this_wrong_answers.append(this_correct_answer)
	this_answers = this_wrong_answers
	#mix in the correct answer
	random.shuffle(this_answers)
	this_index_of_correct = this_answers.index(this_correct_answer)
	#print this_answers,this_index_of_correct
	
	this_question["0"] = this_answers[0]
	this_question["1"] = this_answers[1]
	this_question["2"] = this_answers[2]
	this_question["3"] = this_answers[3]
	this_question["answer"] = this_index_of_correct
	this_question["value"] = 10
	#print this_question
	final_spelling_hard_questions.append(this_question)

#create the vocab questions
final_vocab_questions = []
for x in vocab_questions:
	x = vocab_questions[x]
	this_question = {}
	this_question["title"] = x['word'].capitalize()+": "+ x["phrase"]
	if x['answer']=='a': this_correct_answer = 0
	if x['answer']=='b': this_correct_answer = 1
	if x['answer']=='c': this_correct_answer = 2
	if x['answer']=='d': this_correct_answer = 3
	
	this_question["0"] = x['choices'][0]
	this_question["1"] = x['choices'][1]
	this_question["2"] = x['choices'][2]
	this_question["3"] = x['choices'][3]
	this_question["answer"] = this_correct_answer
	this_question["value"] = 10
	#print this_question
	final_vocab_questions.append(this_question)

"""
Print all the the python dicts to JS dict form, for loading into the web.
All selections are provided to the web, and the web app randomly picks some
for questions.

final_2_letter_questions
final_spelling_easy_questions
final_spelling_hard_questions
final_vocab_questions
"""

print len(final_2_letter_questions),"2 letter questions"
print len(final_spelling_easy_questions),"easy questions"
print len(final_spelling_hard_questions),"hard questions"
print len(final_vocab_questions),"vocab questions"

#print to Javascript dict form:
with open("test_questions.js",'w') as fout:
	fout.write("var two_letter_qs = [];\n")
	fout.write("var easy_qs = [];\n")
	fout.write("var hard_qs = [];\n")
	fout.write("var vocab_qs = [];\n\n")

	for q in final_2_letter_questions:
		line = "two_letter_qs.push({\n"
		line += "    title:  \""+q["title"]+"\",\n"
		line += "    answer:  "+str(q["answer"])+",\n"
		line += "    value:  "+str(q["value"])+",\n"
		line += "    0:  \""+q["0"]+"\",\n"
		line += "    1:  \""+q["1"]+"\",\n"
		line += "    2:  \""+q["2"]+"\",\n"
		line += "    3:  \""+q["3"]+"\",\n"
		line += "});\n"
		fout.write(line)

	for q in final_spelling_easy_questions:
		line = "easy_qs.push({\n"
		line += "    title:  \""+q["title"]+"\",\n"
		line += "    answer:  "+str(q["answer"])+",\n"
		line += "    value:  "+str(q["value"])+",\n"
		line += "    0:  \""+q["0"]+"\",\n"
		line += "    1:  \""+q["1"]+"\",\n"
		line += "    2:  \""+q["2"]+"\",\n"
		line += "    3:  \""+q["3"]+"\",\n"
		line += "});\n"
		fout.write(line)
		
	for q in final_spelling_hard_questions:
		line = "hard_qs.push({\n"
		line += "    title:  \""+q["title"]+"\",\n"
		line += "    answer:  "+str(q["answer"])+",\n"
		line += "    value:  "+str(q["value"])+",\n"
		line += "    0:  \""+q["0"]+"\",\n"
		line += "    1:  \""+q["1"]+"\",\n"
		line += "    2:  \""+q["2"]+"\",\n"
		line += "    3:  \""+q["3"]+"\",\n"
		line += "});\n"
		fout.write(line)

	for q in final_vocab_questions:
		line = "vocab_qs.push({\n"
		line += "    title:  \""+q["title"]+"\",\n"
		line += "    answer:  "+str(q["answer"])+",\n"
		line += "    value:  "+str(q["value"])+",\n"
		line += "    0:  \""+q["0"]+"\",\n"
		line += "    1:  \""+q["1"]+"\",\n"
		line += "    2:  \""+q["2"]+"\",\n"
		line += "    3:  \""+q["3"]+"\",\n"
		line += "});\n"
		fout.write(line)