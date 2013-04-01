import sys
import tweetstream
import re

NUM_TWEETS = 1000
OUTPUT_FILE = "tweets.txt"
TWITTER_UN = "BigBrother2984"
TWITTER_PW = "had416twitter"

def strip_tweet(tweet):
	tweet = re.sub(r'\n', ' ', tweet)
	return tweet

	# tweet = re.sub(r'@\w+:?', '', tweet) # Remove @__
	# tweet = re.sub(r'RT ', '', tweet)
	# tweet = re.sub(r'http:\S+', '', tweet)
	# tweet = re.sub(r'&\S+', '', tweet)
	# # tweet = re.sub(r' \W ', ' ', tweet)
	# tweet = re.sub(r'\[.*?\]', '', tweet)
	# tweet = re.sub(r'[:?!\.()]', '', tweet) # Remove any remaining weird chars
	# tweet = tweet.lstrip()
	# return tweet

def main():

	stream = tweetstream.SampleStream(TWITTER_UN, TWITTER_PW);
	f = open(OUTPUT_FILE, 'w')

	i = 0
	for tweet in stream:
		if (i >= NUM_TWEETS):
			break

		# Ignore non-English tweets.
		if 'lang' not in tweet or tweet['lang'] != 'en':
			continue

		# Ignore tweets with no text.
		if 'text' not in tweet:
			continue
		
		try:
			f.write("%s\n" % strip_tweet(tweet['text']))
			#f.write("%s\n" % tweet['text'])
		except UnicodeEncodeError:
			t = tweet['text'].encode('ascii', 'ignore')
			t = t.decode('utf-8')
			f.write(strip_tweet(t) + "\n")

		i += 1

	f.close()
	return 0


if __name__ == "__main__":	
	sys.exit(main())