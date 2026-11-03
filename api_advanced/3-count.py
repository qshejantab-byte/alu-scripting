#!/usr/bin/python3
"""Counts keywords in the hot titles of a subreddit"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Prints how many times each keyword is in the hot titles"""
    if counts is None:
        counts = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "my-api-script/1.0"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    data = data.get("data")
    posts = data.get("children")
    for post in posts:
        title = post.get("data").get("title")
        title_words = title.lower().split()
        for word in word_list:
            word = word.lower()
            if word not in counts:
                counts[word] = 0
            counts[word] = counts[word] + title_words.count(word)

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    if len(counts) == 0:
        return

    # print the biggest counts first, same counts in alphabetical order
    words = sorted(counts)
    number = max(counts.values())
    while number > 0:
        for word in words:
            if counts[word] == number:
                print("{}: {}".format(word, number))
        number = number - 1
