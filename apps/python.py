# coding: utf-8
from __future__ import unicode_literals
from decorators import on_command

from contextlib import closing
from StringIO import StringIO
import sys


@on_command(['py', 'python'])
def run(robot, channel, user, tokens):
    '''Python 스크립트를 실행 후 결과 출력'''
    code = ' '.join(tokens)
    with closing(StringIO()) as sout:
        sys.stdout = sout

        exec code in {'__builtins__': {}}, {}
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        r_out = sout.getvalue()

    return channel, r_out
