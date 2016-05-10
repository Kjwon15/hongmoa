# coding: utf-8
from __future__ import unicode_literals
from decorators import on_command

from run_code import run_code


@on_command(['repl'])
def run(robot, channel, user, tokens):
    '''스크립트를 실행 후 결과 출력'''
    program = tokens.pop(0)
    code = tokens.pop(0)
    code = "#!/usr/bin/env {}\n{}".format(program, code)
    tokens.insert(0, code)
    return channel, run_code(tokens)
