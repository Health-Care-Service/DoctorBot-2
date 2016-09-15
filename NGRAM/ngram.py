import nltk
from nltk import ngrams

noffiles=1
noofgrams=6
gramdict={}
for fileno in xrange(1,noffiles+1):
	file=open(str(fileno))
	gramdict[fileno]={}
	lines=file.readlines()
	for gram in range(1,noofgrams+1):
		gramdict[fileno][gram]={} 
	for line in lines:
		tokens=nltk.word_tokenize(line.strip('\n\r\t '))
		for gram in range(1,noofgrams+1):
			kgrams=nltk.ngrams(tokens,gram)
			for kgram in kgrams:
				if kgram in gramdict[fileno][gram]:
					gramdict[fileno][gram][kgram]+=1
				else:
					gramdict[fileno][gram][kgram]=1

print gramdict