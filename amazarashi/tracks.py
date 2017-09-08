#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup

from amazarashi.util import access


def get_tracks_data():

    URL = "http://j-lyric.net/artist/a052b38/"
    context = access(URL)

    soup = BeautifulSoup(context, "html.parser")

    result = []

    for item in soup.select(".ttl"):
        result.append(item.text)

    return result
