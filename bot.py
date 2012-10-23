#!/usr/bin/python
import init_twit as tw
import sys, time, re
#import markov
#markovLength = 3
#source_file = '/home/jk/Code/jambot/corpora/corpus.txt'

# optional command line parameters: path/to/corpus_file.txt n-gram_size
if len (sys.argv) >= 2:
	source_file = sys.argv[1]
if len (sys.argv) == 3:
	markovLength = int (sys.argv[2])

if (markov.mapping=={}):
	markov.buildMapping(markov.wordlist(source_file),markovLength)

def genTweet():
	sentence = markov.genSentence(markovLength)
	while (len (sentence) > 130 or len(sentence) < 30):
		sentence = markov.genSentence(markovLength)
	return sentence

while True:
	results = tw.twitter.search(q="@"+tw.handle,since_id=tw.last_id_replied)['results']
	if not results:
		print "Nobody's talking to me...\n"
	jimmies = tw.twitter.search(q="my jimmies",since_id=tw.last_id_replied)['results']
	rustled = [jimi for jimi in jimmies if markov.re.search('rustl*',jimi['text'])]
	results.extend(rustled)
	for result in results:
		question = result['text'].replace('@jmkp','')
		asker = result['from_user']
		status_id = str(result['id'])
		print asker + " said '" + question + "'\n"
		sentence = "We must embrace our jimmies and burn them as fuel for our journey" #genTweet()
		sentence = "@"+asker+" "+sentence
		print status_id+": "+sentence+"\n"
		if tw.last_id_replied < status_id:
			tw.last_id_replied = status_id
		#tw.poster.statuses.update(status=sentence,in_reply_to_status_id=status_id)
	sentence = genTweet()
	print sentence+"\n"
	#tw.poster.statuses.update(status=sentence)
	print "Sweet Dreams...\n"
	time.sleep(10800) # waits for three hours
