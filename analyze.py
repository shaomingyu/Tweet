#!/usr/bin/env python3
from functools import *
import json
import operator
with open("tweets.json", "r") as tweet_db:
	tweets = json.load(tweet_db)
# TODO: implement assigned functions

def flatten(xs):
	return reduce(lambda x, y: x + y, xs)

def difference(xs, ys):
	return list(filter(lambda x: x not in ys, xs)) + list(filter(lambda x: x not in xs, ys))

def to_text(tweets):
	return list(map(lambda x: x["content"], tweets))

def to_lowercase(tweets):
	return map(lambda x: dict(x, content = x["content"].lower()), tweets)

def nonempty(tweets):
	return list(filter(lambda x: x["content"], tweets))

def word_count(tweets):
	return reduce(lambda x, y: x + y, map(lambda x: len(x["content"].split()), tweets))

def hashtags(tweet):
	return list(filter(lambda x: x.startswith("#"), tweet["content"].split()))

def mentions(tweet):
	return list(filter(lambda x: x.startswith("@"), tweet["content"].split()))

def all_hashtags(tweets):
	return flatten(list(map(lambda x: hashtags(x), tweets)))

def all_mentions(tweets):
	return flatten(list(map(lambda x: mentions(x), tweets)))

def all_words(tweets):
	return flatten(list(map(lambda x: x["content"].split(" "), tweets)))

def all_caps_tweets(tweets):
	return list(filter(lambda x: x["content"] == x["content"].upper(), tweets))

def count_individual_words(tweets):
	return reduce(lambda x, y: ((dict(x, **{y: x[y] + 1}) if y in x.keys() else dict(x, **{y:1})) if type(x) is dict else {x:1}), all_words(tweets))

def count_individual_hashtags(tweets):
	return reduce(lambda x, y: ((dict(x, **{y: x[y] + 1}) if y in x.keys() else dict(x, **{y:1})) if type(x) is dict else {x:1}), all_hastags(tweets))
	
def count_individual_mentions(tweets):
	return reduce(lambda x, y: ((dict(x, **{y: x[y] + 1}) if y in x.keys() else dict(x, **{y:1})) if type(x) is dict else {x:1}), all_mentions(tweets))
	
def n_most_common(n, word_count):
	return list(sorted(word_count.items(), key=lambda x: (-x[1], x[0])))[:n]

def iphone_tweets(tweets):
	return list(filter(lambda x: "iPhone" in x["source"], tweets))

def android_tweets(tweets):
	return list(filter(lambda x: "Android" in x["source"], tweets))

def average_favorites(tweets):
	return reduce(lambda x, y: x["favorites"] + y["favorites"] if type(x) is dict else x + y["favorites"], tweets)/ len(tweets)

def average_retweets(tweets):
	return reduce(lambda x, y: x["retweets"] + y["retweets"] if type(x) is dict else x + y["retweets"], tweets)/ len(tweets)

def sort_by_favorites(tweets):
	return list(sorted(tweets, key = lambda x: (x["favorites"])))

def sort_by_retweets(tweets):
	return list(sorted(tweets, key = lambda x: (x["retweets"])))

def upper_quartile(tweets):
	return tweets[round(3/4*len(tweets))]

def lower_quartile(tweets):
	return tweets[round(1/4*len(tweets))]

def top_quarter_by(tweets, factor):
	return tweets[round(3/4 * len(tweets))]

def lower_quarter_by(tweets, factor):
	return tweets[round(1/4 * len(tweets))]