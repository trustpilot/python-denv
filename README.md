# denv

```
denv COMMAND [ARGS]
```

Expects a `.env` file in current directory of format:

```
KEY=VALUE
KEY=host=foo user=bar
```

### Example

```
$ cat .env
CONNECTION_STRING=host=foo user=bar password=baz

$ denv env | grep CONNECTION_STRING
host=foo user=bar password=baz
```

## Why?

so many dotenv repos exist out there but none of them (AFAIK) can read connection string formatted values like `connection_string=host=foo user=bar password=baz`.

So here is a very simple cli script to do just that! :-)
