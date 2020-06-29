## General guidelines

Be sure to go through these items before creating a new issue:

1. Check the [existing issues](https://github.com/gleitz/howdoi/issues) to see if anyone is already working or have already worken on your issue or a similar one.

2. If there are no current or past issues similar to yours, be sure to give a a **complete description** when creating it.

3. Wait for feedback on the issue before starting to work.

!!! tip
    Include instructions on how to reproduce the bug you found or specific use cases of a requested feature.

!!! Note
    Follow Github's [guide to collaborating efficiently](https://lab.github.com/githubtraining/introduction-to-github).



## Setting up development environment

Clone the git repository
```bash
$ git clone https://github.com/gleitz/howdoi.git
```

Setup and activate a virtual environment
```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Install packages
```bash
$ pip install -r requirements.txt
```

## Running howdoi

Run on the command-line
```bash
python -m howdoi.howdoi QUERY
```

!!! note
    If you try running `python howdoi/howdoi.py` (without `-m`) you might get `ValueError: Attempted relative import in non-package`.

If you want to use howdoi from within a python script, just pass your query to `howdoi.howdoi()`

```python
from howdoi import howdoi

query = "for loop python"
output = howdoi.howdoi(query)
```

Or parse it yourself and passed the arguments to `howdoi.howdoi()`
```python
from howdoi import howdoi

query = "for loop python"
parser = howdoi.get_parser()
args = vars(parser.parse_args(query.split(' ')))

output = howdoi.howdoi(args)
```

!!! attention
    Parsing queries yourself is the older way to pass in queries and may be deprecated in the future. Prefer the first example.


## Submitting Pull Requests
Before PRs are accepted they must pass all [Travis tests](https://travis-ci.org/gleitz/howdoi) and not have any `flake8` or `pylint` warnings or errors.

#### Testing
Howdoi uses python's [`unittest`](https://docs.python.org/3/library/unittest.html) library for unit testing. Run the unit tests locally

```bash
$ python -m test_howdoi
```

It's also possible to run only specific tests

```bash
$ python -m unittest test_howdoi.TestClass.test_method
```

Make sure all tests pass before submitting a PR.

!!! tip
    Remmember to run the tests while inside the virtual environment (run `source .venv/bin/activate` to activate it).

#### Linting
Run linting locally with [`flake8`](https://flake8.pycqa.org/en/latest/)
```bash
$ flake8
```
Or [`pylint`](https://www.pylint.org/)
```bash
$ pylint *
```

!!! tip
    Howdoi uses vanilla configuration files for both linters (`.flake8rc` and `.pylintrc` in the root directory), but with a max line length of 119 characters.


