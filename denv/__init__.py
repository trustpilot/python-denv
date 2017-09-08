__author__ = 'sloev.github.io'

import sys
import subprocess
from os import environ


def main():
    args = sys.argv
    try:
        args[1]
        env_file = open('.env', 'r')
    except IndexError:
        print("usage: denv COMMAND [ARGS]\ndenv expects a .env file to be present in current folder")
        exit(0)
    except FileNotFoundError:
        print("denv expects a .env file to be present in current folder")
        exit(1)

    env = environ.copy()
    lines = env_file.read().split("\n")
    for line in lines:
        if line:
            key, value = line.split('=', 1)
            env[key] = value
    exit_code = subprocess.Popen(args[1:], env=env).wait()
    exit(exit_code)


if __name__ == "__main__":
    main()
