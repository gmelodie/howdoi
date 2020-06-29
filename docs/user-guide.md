## Usage

If that's your first time using howdoi, run the quick help

```bash
$ howdoi howdoi
```


Print the help manual
```bash
$ howdoi # "howdoi -h" also prints help


usage: howdoi.py [-h] [-p POS] [-a] [-l] [-c] [-n NUM_ANSWERS] [-C]
                 [-v] [-e ENGINE] QUERY [QUERY ...]

instant coding answers via the command line

positional arguments:
  QUERY                 the question to answer

optional arguments:
  -h, --help            show this help message and exit
  -p POS, --pos POS     select answer in specified position (default: 1)
  -a, --all             display the full text of the answer
  -l, --link            display only the answer link
  -c, --color           enable colorized output
  -n NUM_ANSWERS, --num-answers NUM_ANSWERS
                        number of answers to return
  -C, --clear-cache     clear the cache
  -v, --version         displays the current version of howdoi
  -e ENGINE, --engine ENGINE  change search engine for this query only.
                              Currently supported engines: google (default),
                              bing, duckduckgo.
```
