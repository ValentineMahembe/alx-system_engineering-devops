#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subcribers for a given reddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function to return the number of subcribers for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'vmahembe'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get("data").get("subscribers")
    else:
        return 0
