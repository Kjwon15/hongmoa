# coding: utf-8
from __future__ import unicode_literals
from decorators import on_command
from run_code import run_code

@on_command(['py3'])
def run(robot, channel, user, tokens):
    ''' Run Python3 script'''
    code = tokens[0]
    tokens[0] = '#!/usr/bin/env python3\n\n' + code
    return channel, run_code(tokens)
