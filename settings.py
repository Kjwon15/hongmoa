# coding: utf-8
from __future__ import unicode_literals

import os


APPS = ['hello_world', 'helper', 'python', 'repl']

SLACK_TOKEN = os.environ.get('SLACK_TOKEN')


REDIS_URL = None
