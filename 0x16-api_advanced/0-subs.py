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

    if response.status_code != 200:
        return 0
    return response.json().get("data").get("subscribers")


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
