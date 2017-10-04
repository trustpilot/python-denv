__author__ = 'sloev.github.io'

import sys
import subprocess
from os import environ


def main(command_args, env_file_lines):
    env = environ.copy()
    for line in env_file_lines:
        if line:
            key, value = line.split('=', 1)
            env[key] = value
    exit_code = subprocess.Popen(command_args, env=env).wait()
    exit(exit_code)


if __name__ == "__main__":
    args = sys.argv
    command_line = ""
    env_file_lines = []
    try:
        args[1]  # noqa
        command_line = args[1:]
        env_file = open('.env', 'r')
        env_file_lines = env_file.read().split("\n")
    except IndexError:
        print("usage: denv COMMAND [ARGS]\ndenv expects a .env file to be present in current folder")
        exit(0)
    except FileNotFoundError:  # noqa
        print("denv expects a .env file to be present in current folder")
        exit(1)

    main(command_line, env_file_lines)
