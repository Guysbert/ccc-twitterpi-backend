import ConfigParser
import twitter
import json

config = ConfigParser.ConfigParser()
config.read('config.ini')

consumer_key = config.get('Consumer', 'consumer_key')
consumer_secret = config.get('Consumer', 'consumer_secret')
access_token_key = config.get('Access', 'access_token_key')
access_token_secret = config.get('Access', 'access_token_secret')

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)


def update_tweets():
    data = []
    for tweet in api.GetSearch('#cccamp15', result_type='recent'):
        tweet_data = dict()
        tweet_images = list()
        if len(tweet.media) > 0:
            for medium in tweet.media:
                tweet_images.append(medium['media_url_https'])
        tweet_data['images'] = tweet_images
        tweet_data['text'] = tweet.text
        tweet_data['user'] = "@" + tweet.user.screen_name
        data.append(tweet_data)
    return json.dumps(data, ensure_ascii=False).encode('utf-8')

