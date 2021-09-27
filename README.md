# Cookiecutter Logtalk

A script for setting up Logtalk projects

## What's included?

See [cookiecutter.readthedocs.io](https://cookiecutter.readthedocs.io/) for
more information about Cookiecutter.

- Stub files for:
	- `loader.lgt`
	- `<my_project.lgt>`
	- `tester.lgt`
	- `tests.lgt`
	- `.gitignore`
	- `README.md`
- Optionally copy Logtalk's `settings-sample.lgt` to the project as
  `settings.lgt`
- Optionally `git init` the project

## Requirements

Cookiecutter is a Python3 tool, this script requires Python version >= 3.4 with
cookiecutter installed:

```bash
$~: python3 -m pip install cookiecutter
```

To be able to copy the settings file you also need Logtalk installed with
either the `$LOGTALKHOME` or `$LOGTALKUSER` environment variables set, which is
part of the Logtalk installation process. `$LOGTALKUSER` is prefered over
`$LOGTALKHOME` and the `settings-sample.lgt` file will be copied from there if
found.

## Get Started

Do not create a directory for your project, one will be created for you.

### With `cookiecutter`

Cookiecutter can download and run this template with:

```bash
$~: cookiecutter https://github.com/PaulBrownMagic/cookiecutter-logtalk
```

Then follow the prompts to create your application.

### With lgtinit

We've included a `lgtinit` Python script that provides nicer default values
than plain cookiecutter, such as trying to determine the author name from your
git config, falling back to the `$USER` environment variable. It saves a little
time and typing.

```bash
$~: mkdir ~/.cookiecutters
$~: git clone https://github.com/PaulBrownMagic/cookiecutter-logtalk ~/.cookiecutters/
$~: ~/.cookiecutters/lgtinit
```

I like to either create a soft-link/shortcut in my local bin directory to the
`lgtinit` script, or set it as an alias for ease of use.
