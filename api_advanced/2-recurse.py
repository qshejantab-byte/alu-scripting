#!/usr/bin/python3
"""Gets the titles of all the hot posts of a subreddit with recursion"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Returns a list with the titles of all hot posts, None if no results"""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "my-api-script/1.0"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    for post in data.get("children"):
        hot_list.append(post.get("data").get("title"))

    after = data.get("after")
    if after is not None:
        return recurse(subreddit, hot_list, after)

    if len(hot_list) == 0:
        return None
    return hot_list
