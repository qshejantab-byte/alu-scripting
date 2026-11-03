#!/usr/bin/python3
"""Counts the keywords in the titles of the hot posts of a subreddit"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Prints the sorted count of the keywords found in the hot titles"""
    if counts is None:
        counts = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "my-api-script/1.0"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data")
    for post in data.get("children"):
        title = post.get("data").get("title").lower().split()
        for word in word_list:
            word = word.lower()
            counts[word] = counts.get(word, 0) + title.count(word)

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    results = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    for word, count in results:
        if count > 0:
            print("{}: {}".format(word, count))
