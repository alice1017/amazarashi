#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
from urlparse import urljoin
from amazarashi.util import access


def get_lyric_link(track):

    URL = "http://j-lyric.net/artist/a052b38/"
    context = access(URL)
    soup = BeautifulSoup(context, "html.parser")

    for item in soup.select(".ttl"):
        child = list(item.children)[0]
        track_title = child.text

        if track_title == track:
            result = child.get("href")

    base_link = "http://j-lyric.net/artist/a052b38/"
    return urljoin(base_link, result)


def get_lyrics_data(URL):

    context = access(URL)

    soup = BeautifulSoup(context, "html.parser")
    lyric = soup.select("#Lyric")[0].renderContents()

    replace_data = {
        "<br>": "\n", "</br>": "", "<br/>": ""
    }
    for key, value in replace_data.iteritems():
        lyric = lyric.replace(key, value)

    return lyric
