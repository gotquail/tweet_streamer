import sys
import tweetstream

NUM_TWEETS = 20

def main():

	stream = tweetstream.SampleStream("BigBrother2984", "had416twitter");
	f = open('tweets.txt', 'w')

	i = 0
	for tweet in stream:
		if (i >= NUM_TWEETS):
			break

		# Ignore non-English tweets.
		if 'lang' in tweet:
			if tweet['lang'] != 'en':
				continue

			t = str(tweet).encode('ascii', 'ignore') # encode to ascii
			f.write(str(t) + '\n')


		# # Only print the tweet text.
		# if 'text' in tweet:
		# 	f.write(str(tweet['text'].encode('ascii', 'ignore')) + "\n")

		# i += 1

	f.close()
	return 0


if __name__ == "__main__":	
	sys.exit(main())