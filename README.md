# denv

[![Build Status](http://travis-ci.org/trustpilot/python-denv.svg?branch=master)](https://travis-ci.org/trustpilot/python-denv)  [![Latest Version](https://img.shields.io/pypi/v/denv.svg)](https://pypi.python.org/pypi/denv) [![Python Support](https://img.shields.io/pypi/pyversions/denv.svg)](https://pypi.python.org/pypi/denv)

Run your **script** with your **env** 

Ultra simple runner that injects vars from the implicit `.env` file into your commands of choice.

```
denv COMMAND [ARGS]
```

Expects a `.env` file in the current directory of format:

```
KEY=VALUE
FOO=BAR
AGE=29
host=hostname=foo user=bar password=false
```

### Examples

Create an `.env` file holding your vars
```bash
$ cat .env
CONNECTION_STRING=host=foo user=bar password=baz
```

Use them in posix commands:
```bash
$ denv env | grep CONNECTION_STRING
host=foo user=bar password=baz
```

Use them when running python scripts:
```bash
$ denv python -c 'import os;print(os.environ["host"])'
foo user=bar password=baz
```

## Why?

At Trustpilot we strictly follow the [12-factors](https://12factor.net) of designing software-as-a-service apps,
especially the concept of [isolating your configuration](https://12factor.net/config) outside your app.

Using environment vars is the accepted practice for injecting these configs into apps during deployment. 
But running locally i wanted something very simple to inject these `env-vars` into the runtime myself.

Looking around you will quickly find many implementations:

* https://direnv.net/
* https://github.com/bkeepers/dotenv
* https://github.com/motdotla/dotenv
* https://github.com/pedroburon/dotenv
* https://github.com/josegonzalez/php-dotenv

But i tend to disagree with them in two ways:

1. They tend to aim for being a replacement for your runtimes default `environment` lib and just overload with reading from a file
2. [Some](https://direnv.net/) of them lack support for *connection-strings* where there can be many `=`'s per line.

I wanted to seperate it completely so the runtime only cared about `env-vars` and its standard way of accessing these, 
and then have the **runner** inject these vars as the only thing it did.

*- [sloev](sloev.github.io)*

