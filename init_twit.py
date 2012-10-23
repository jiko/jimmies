from twitter import Twitter, TwitterError
from twitter.oauth import OAuth, read_token_file
from twitter.oauth_dance import oauth_dance
import os

# get your own at https://dev.twitter.com/apps/new
CONSUMER_KEY='bns94SYmy79jmQEOArj5g'
CONSUMER_SECRET='YCkH7PocJ4zZAY9f5snyVjNBZRwJRcE5SEVEhaUZ8GQ'

# path to where your oauth credentials are stored 
oauth_filename = os.environ.get('HOME', '') + os.sep + '.rc_twitter_oauth'
# use the function 'from twitter.oauth import write_token_file' to create this file
oauth_token, oauth_token_secret = read_token_file(oauth_filename)

twitter = Twitter(domain='search.twitter.com')
twitter.uriparts = ()

poster = Twitter(
	auth=OAuth(
		oauth_token, oauth_token_secret, CONSUMER_KEY, CONSUMER_SECRET),
		secure=True,
		api_version='1',
		domain='api.twitter.com')

# get the status_id of the last tweet to which you replied
last_id_replied = [tweet['in_reply_to_status_id'] for tweet in poster.statuses.user_timeline() if tweet['in_reply_to_status_id'] != None][0]
# your bot's twitter handle
handle = "RustleCrowe"
