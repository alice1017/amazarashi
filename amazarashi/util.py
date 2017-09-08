#!/usr/bin/env python
# coding: utf-8

import chardet
import requests


def access(url):

    context = requests.get(url)._content
    encoding = chardet.detect(context)["encoding"]
    return context.decode(encoding, "")
