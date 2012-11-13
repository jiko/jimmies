#!/usr/bin/python
import init_twit as tw
import time, re, random, os

def log(msg):
	with open('log','a') as f:
		f.write(msg+"\n")
	print msg

def fileToList(filename):
	with open(filename) as f:
		return [line.strip() for line in f]

tweet_files = ['lines.txt','responses.txt','replies.txt']
tweets = dict([ (os.path.splitext(name)[0], fileToList(name)) for name in tweet_files ])

def tweet(seq,irtsi=None,at=None): 
	status = random.choice(tweets[seq])
	try:
		if at and irtsi:
			status = "@"+at+" "+status
			tw.poster.statuses.update(status=status,in_reply_to_status_id=irtsi)
		else:
			tw.poster.statuses.update(status=status)
	except tw.TwitterError as error:
		log("".join(error.args))
	else:
		if irtsi: 
			status = "In reply to "+irtsi+": "+status
		log(status)

def reply(mention,seq):
	asker = mention['from_user']
	log(asker + " said " + mention['text'])
	status_id = str(mention['id'])
	if tw.last_id_replied < status_id:
		tw.last_id_replied = status_id
	tweet(seq,status_id,asker)


while True:
	unrustled = re.compile('rt\s|unrustl|thank|lo+l|laugh|hah|rofl|lmf?aoi|stahp',flags=re.I)
	results = tw.twitter.search(q="@"+tw.handle,since_id=tw.last_id_replied)['results']
	results = [t for t in results if not unrustled.search(t['text'])]
	if results:
		[reply(result,'replies') for result in results]
	else:
		log("No replies necessary...")
	rustled = re.compile('rustl',flags=re.I)
	jimmies = tw.twitter.search(q="my jimmies",since_id=tw.last_id_replied)['results']
	jimmies = [jimi for jimi in jimmies if rustled.search(jimi['text'])]
	jimmies = [j for j in jimmies if not unrustled.search(j['text'])]
	if jimmies:
		log("I detect a rustling in the jimmies...")
		reply(jimmies[0],"responses") # Bulk unsolicited mentions will get you suspended
	else:
		log("Nobody's jimmies are rustled...")
	tweet('lines')
	log("Sweet Dreams...")
	time.sleep(7200) # waits for two hours
