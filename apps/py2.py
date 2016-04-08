# coding: utf-8
from __future__ import unicode_literals
from decorators import on_command
from run_code import run_code

@on_command(['py2'])
def run(robot, channel, tokens):
    ''' Run Python2 script'''
    code = tokens[0]
    tokens[0] = '#!/usr/bin/env python2\n\n' + code
    return run_code(tokens)
