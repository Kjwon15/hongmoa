# coding: utf-8
from __future__ import unicode_literals
from decorators import on_command

from tempfile import NamedTemporaryFile
import os
import subprocess


@on_command(['repl'])
def run(robot, channel, tokens):
    '''스크립트를 실행 후 결과 출력'''
    code = ' '.join(tokens).strip()

    script_file = NamedTemporaryFile(delete=True)

    with open(script_file.name, 'w') as fp:
        fp.write(code)

    os.chmod(script_file.name, 0755)
    script_file.file.close()

    process = subprocess.Popen(
        [script_file.name],
        env={},
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    process.wait()
    stdout, stderr = process.communicate()

    return stderr or stdout
