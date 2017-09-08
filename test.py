#!/usr/bin/env python
# coding: utf-8

import unittest

from amazarashi.util import (
    access,
    check_peco_exist
)
from amazarashi.tracks import get_tracks_data
from amazarashi.lyrics import (
    get_lyric_link,
    get_lyrics_data
)


class Tester(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_tracks_data(self):

        tracks = get_tracks_data()
        self.assertEqual(tracks[0], u"14歳")

    def test_lyric_link(self):

        track = u"終わりで始まり"
        track_link = "http://j-lyric.net/artist/a052b38/l02f1ad.html"

        self.assertEqual(get_lyric_link(track), track_link)

    def test_lyric(self):

        track = u"空に歌えば"
        track_link = "http://j-lyric.net/artist/a052b38/l042264.html"

        self.assertEqual(get_lyric_link(track), track_link)

        lyric = get_lyrics_data(track_link)
        lyric_head = "虚実を切り裂いて 蒼天を仰いで 飛び立った永久"

        self.assertEqual(
            lyric.split("\n")[0], lyric_head)

    def test_check_peco(self):

        self.assertTrue(check_peco_exist())

    def test_access(self):

        URL = "http://httpbin.org/user-agent"
        RETURNS = u'{\n  "user-agent": "python-requests/2.13.0"\n}\n'

        context = access(URL)

        self.assertEqual(context, RETURNS)

if __name__ == '__main__':

    unittest.main(verbosity=2)
