__author__ = 'sloev.github.io'

import argparse
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--env-file', '-e', \
            metavar="ENV_FILE", \
            type=argparse.FileType('r'), \
            default='.env', \
            help='Environment file to read from, defaults to .env')

    parser.add_argument('command', nargs=1, help='Command to run')
    parser.add_argument('command_args', nargs=argparse.REMAINDER)
    args = parser.parse_args()

    command_line = ""
    env_file_lines = []
    command_line = args.command + args.command_args
    env_file_lines = args.env_file.read().split("\n")

    main(command_line, env_file_lines)
