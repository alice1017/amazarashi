#!/usr/bin/env python
# coding: utf-8

import sys
import chardet
import requests

from subprocess import Popen


def access(url):

    context = requests.get(url)._content
    encoding = chardet.detect(context)["encoding"]
    return context.decode(encoding, "")


def check_peco_exist():

    cmd = "type peco"
    proc = Popen(cmd, stdin=-1, stdout=-1, stderr=-1, shell=True)
    proc.wait()
    exit_code = proc.returncode

    if exit_code is not 0:
        sys.stderr.write(
            u"pecoがインストールされていません\n")
        sys.exit(1)
