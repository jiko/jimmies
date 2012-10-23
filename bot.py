#!/usr/bin/python
import init_twit as tw
import time, re, random

lines = ["There is no need to be upset",
	"My jimmies remain unrustled",
	"Across the vast and majestic gulf of time and space the jimmies rustle softly",
	"EVERYBODY'S GETTING RUSTLED",
	"Did I just hear some rustling?"]

responses = [
	"We must embrace our jimmies and burn them as fuel for our journey",
	"Shh no tears only dreams now",
	"Awaken child, and embrace the glory of your jimmies",
	"http://www.youtube.com/watch?v=07wZiqJlu3U",
	"http://www.youtube.com/watch?v=ygr5AHufBN4",
	"http://www.youtube.com/watch?v=oScCgxuId98",
	"http://www.youtube.com/watch?v=_1MSv2fIsbA",
	"http://www.youtube.com/watch?v=I0D1M3xneS8",
	"http://www.youtube.com/watch?v=vBlX86yVEVs",
	"http://www.youtube.com/watch?v=vaXcd5-BCTY",
	"http://www.youtube.com/watch?v=MGayPWHjyIY",
	"http://www.youtube.com/watch?v=Md7fY_ql0fg",
	"http://www.youtube.com/watch?v=a6rFgflr5yo",
	"http://www.youtube.com/watch?v=y6ASBE0sVpQ"
	]

def genTweet(seq):
	return random.choice(seq)

while True:
	results = tw.twitter.search(q="@"+tw.handle,since_id=tw.last_id_replied)['results']
	if not results:
		print "Nobody's talking to me...\n"
	#jimmies = tw.twitter.search(q="my jimmies",since_id=tw.last_id_replied)['results']
	#rustled = [jimi for jimi in jimmies if re.search('rustl*',jimi['text'])]
	#results.extend(rustled)
	for result in results:
		question = result['text'].replace('@jmkp','')
		asker = result['from_user']
		status_id = str(result['id'])
		print asker + " said '" + question + "'\n"
		sentence = genTweet(responses)
		sentence = "@"+asker+" "+sentence
		print status_id+": "+sentence+"\n"
		if tw.last_id_replied < status_id:
			tw.last_id_replied = status_id
		tw.poster.statuses.update(status=sentence,in_reply_to_status_id=status_id)
	sentence = genTweet(lines)
	print sentence+"\n"
	tw.poster.statuses.update(status=sentence)
	print "Sweet Dreams...\n"
	time.sleep(10800) # waits for three hours
