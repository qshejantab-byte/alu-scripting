#!/usr/bin/python3
"""Gets the number of subscribers of a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers, 0 if the subreddit is not valid"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "my-api-script/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    if data is None:
        return 0
    return data.get("subscribers", 0)
