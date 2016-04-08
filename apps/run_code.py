from tempfile import NamedTemporaryFile
import os
import subprocess

def run_code(tokens):
    code = tokens[0].strip()
    try:
        stdin = tokens[1]
    except IndexError:
        stdin = None

    script_file = NamedTemporaryFile(delete=True)

    with open(script_file.name, 'w') as fp:
        fp.write(code)

    os.chmod(script_file.name, 0755)
    script_file.file.close()

    process = subprocess.Popen(
        [script_file.name],
        env={},
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    if stdin:
        process.stdin.write(stdin)
        process.stdin.close()
    process.wait()
    stdout = process.stdout.read()
    stderr = process.stderr.read()

    return stderr or stdout
