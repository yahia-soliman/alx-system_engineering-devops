#!/usr/bin/python3
"""get a list of the titles of posts listed for a given subreddit"""
import requests


def get_posts(subreddit, after=""):
    """I'm the only function here"""
    url = "https://www.reddit.com/r/{sub}/hot.json".format(sub=subreddit)
    params = {"limit": 100, "after": after}
    headers = {
        "User-Agent": "yahia:intranet.alxswe.com:v2.4.1 (by /u/keroxyz)",
    }
    res = requests.get(url=url, headers=headers, params=params)
    if res.status_code != 200:
        return None, None
    data = res.json()["data"].get("children")
    if not data:
        return None, None
    return data, res.json()["data"].get("after")


def count_words(subreddit, word_list, counter=None, after=""):
    """I'm the only function here"""
    if counter is None:
        if not word_list or not len(word_list):
            return None
        counter = dict([(word.lower(), 0) for word in word_list])
        word_list = counter.keys()
    posts, after = get_posts(subreddit, after)
    if not posts:
        return None
    for post in posts:
        title = post["data"].get("title", "").lower().split(" ")
        for word in word_list:
            counter[word] += title.count(word)
    if after:
        count_words(subreddit, word_list, counter, after)
    else:
        items = sorted(counter.items(), key=lambda i: i[1], reverse=True)
        for key, val in items:
            if key and val:
                print("{}: {}".format(key, val))
