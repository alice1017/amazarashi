#!/usr/bin/env python
# coding: utf-8

import os
import sys
import codecs

from urlparse import urljoin
from subprocess import Popen

from amazarashi.tracks import get_tracks_data
from amazarashi.lyrics import (
    get_lyric_link,
    get_lyrics_data
)


def check_peco_exist():

    cmd = "type peco"
    proc = Popen(cmd, stdin=-1, stdout=-1, stderr=-1, shell=True)
    proc.wait()
    exit_code = proc.returncode

    if exit_code is not 0:
        sys.stderr.write(
            u"pecoがインストールされていません\n")
        sys.exit(1)


def choice_tracks(tracks):

    check_peco_exist()

    # make temporary file contained tracks data
    filename = "/tmp/amazarashi_tracks.txt"
    with codecs.open(filename, "w", "utf-8") as fp:
        fp.write(u"\n".join(tracks))

    # run peco process
    cmd = "cat {} | peco".format(filename)
    proc = Popen(cmd, stdin=-1, stdout=-1, stderr=-1, shell=True)
    proc.wait()
    out, err = proc.communicate()

    # remove tempfile
    os.remove(filename)

    if not err:
        return unicode(out.strip("\n"), "utf-8")


def main():

    tracks_data = get_tracks_data()
    track = choice_tracks(tracks_data)
    print u"曲：{0}".format(track)

    link = get_lyric_link(track)
    base_link = "http://j-lyric.net/artist/a052b38/"
    track_link = urljoin(base_link, link)

    print get_lyrics_data(track_link)

if __name__ == '__main__':

    main()
