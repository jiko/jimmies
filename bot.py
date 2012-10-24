#!/usr/bin/python
import init_twit as tw
import time, re, random

lines = ["There is no need to be upset",
	"My jimmies remain unrustled",
	"Across the vast and majestic gulf of time and space the jimmies rustle softly",
	"EVERYBODY'S GETTING RUSTLED",
	"Did I just hear some rustling?",
	"Our jimmies are eternal. None can rustle the Triumvirate.",
	"What we jimmie in life rustles in eternity",
	"We control the jimmies. We control the rustling.",
	"You cannot even imagine how unrustled our jimmies are",
	"Are your jimmies rustled?",
	"Seems like your jimmies are rustled.",
	"Are you not rustled?",
	"I felt a great disturbance in the jimmies, as if millions of jimmies were suddenly rustled at once"
	"One does not simply rustle my jimmies",
	"For it is foretold that on the day of the great rustling, no mortal shall life in fear." 
	]

responses = [
	"We must embrace our jimmies and burn them as fuel for our journey",
	"Shh no tears only dreams now",
	"Awaken child, and embrace the glory of your jimmies",
	"http://www.youtube.com/watch?v=07wZiqJlu3U",
	"http://www.youtube.com/watch?v=ygr5AHufBN4",
	"http://www.youtube.com/watch?v=oScCgxuId98",
	"http://www.youtube.com/watch?v=_1MSv2fIsbA",
	"http://www.youtube.com/watch?v=I0D1M3xneS8",
	"http://www.youtube.com/watch?v=vaXcd5-BCTY",
	"http://www.youtube.com/watch?v=MGayPWHjyIY",
	"http://www.youtube.com/watch?v=Md7fY_ql0fg",
	"http://www.youtube.com/watch?v=a6rFgflr5yo",
	"http://www.youtube.com/watch?v=y6ASBE0sVpQ",
	"http://www.youtube.com/watch?v=9KFJCSgDml8",
	"http://www.youtube.com/watch?v=9uvIGrnA_3I",
	"http://www.youtube.com/watch?v=oVU2gY1B4Qw",
	"http://www.youtube.com/watch?v=6w_DQhsqsCw"
	]

def genTweet(seq):
	return random.choice(seq)

while True:
	sentence = genTweet(lines)
	#tw.poster.statuses.update(status=sentence)
	print sentence+"\n"
	results = []
	results = tw.twitter.search(q="@"+tw.handle,since_id=tw.last_id_replied)['results']
	if not results:
		print "Nobody's talking to me...\n"
	else: #filter replies list
		unrustled = re.compile('rt|unrustl*|thank*|lol|laugh*|ha*')
		results = [tweet for tweet in results if !unrustled.search(tweet['text'],flags=re.IGNORECASE)]
	jimmies = tw.twitter.search(q="my jimmies",since_id=tw.last_id_replied)['results']
	rustled = [jimi for jimi in jimmies if re.search('rustl*',jimi['text'].lower())]
	if rustled:
		results.append(rustled[0])
	else:
		print "Nobody's jimmies are rustled...\n"
	for result in results:
		asker = result['from_user']
		print asker + " said " + result['text']
		status_id = str(result['id'])
		sentence = "@"+asker+" "+genTweet(responses)
		print status_id+": "+sentence+"\n"
		if tw.last_id_replied < status_id:
			tw.last_id_replied = status_id
		#tw.poster.statuses.update(status=sentence,in_reply_to_status_id=status_id)
	print "Sweet Dreams...\n"
	time.sleep(3600) # waits for one hour
