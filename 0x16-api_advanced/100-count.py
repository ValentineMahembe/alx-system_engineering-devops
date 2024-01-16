#!/usr/bin/python3
"""
Queries the Reddit API, parses the title of all hot articles, and prints a
sorted count of given keywords.
"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, word_count=Counter()):
    """
    Recursive function to print a sorted count of given keywords found in the
    titles of all hot articles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'custom'}
    if after:
        url += "?after={}".format(after)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return
    data = response.json().get("data")
    for post in data.get("children"):
        title = post.get("data").get("title").lower().split()
        word_count += Counter(word for word in title if word in word_list)
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, word_count)
    else:
        word_count = dict(word_count)
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print("{}: {}".format(word, count))


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        word_list = [x.lower() for x in sys.argv[2].split()]
        count_words(sys.argv[1], word_list)
