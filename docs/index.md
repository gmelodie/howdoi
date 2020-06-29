# HowDoI
Never have open your browser to look for answers again.

Create tar archive:
```bash
$ howdoi create tar archive
> tar -cf backup.tar --exclude "www/subf3" www
```

Format a date in bash:
```bash
$ howdoi format date bash
> DATE=`date +%Y-%m-%d`
```
Print stack trace in Python:
``` bash
$ howdoi print stack trace python
> import traceback
>
> try:
>     1/0
> except:
>     print '>>> traceback <<<'
>     traceback.print_exc()
>     print '>>> end of traceback <<<'
> traceback.print_exc()
```

```bash
$ howdoi convert mp4 to animated gif
> video=/path/to/video.avi
> outdir=/path/to/output.gif
> mplayer "$video" \
>         -ao null \
>         -ss "00:01:00" \  # starting point
>         -endpos 10 \ # duration in second
>         -vo gif89a:fps=13:output=$outdir \
>         -vf scale=240:180
```


## Here are some example alerts you can use
##### These are from the [Adomonition](https://python-markdown.github.io/extensions/admonition/) extension

!!! attention
    attention alert

!!! caution
    caution alert

!!! danger
    danger alert

!!! error
    error alert

!!! hint
    hint alert

!!! important
    important alert

!!! note
    note alert

!!! tip
    tip alert

!!! warning
    warning alert

!!! Custom alert
    Custom alert

Alternatively you can use the `!!! type "Custom Title"` format to get the correct type emoji and use any title you want like so:

!!! tip "Tip type alert but with a custom title"
    they're good aren't they

## Include source code in 1 line of code

To import code we can use this syntax inside of a code block with the language label:  "{\!path/to/file\!}".

Here's `../howdoi/__init__.py`

```Python
{!../howdoi/__init__.py!}
```

## Here is a choice tab
Proper syntax highlighted code blocks in these don't work the way you'd think and I don't know how to get them to work normally without some extension

=== "Python"
    To do x in python use this code:

    ```python
    def main():
        print("Hello world")
    if __name__ == "__main__":
        main()
    ```

=== "Golang"
    To do x in golang use this code:

    ```go
    package main
    import "fmt"
    func main() {
        fmt.Println("Hello world")
    }
    ```


## Commands

* `python -m mkdocs new [dir-name]` - Create a new project.
* `python -m mkdocs serve` - Start the live-reloading docs server.
* `python -m mkdocs build` - Build the documentation site.
* `python -m mkdocs help` - Print this help message.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.


```Python
{!../howdoi/__init__.py!}
```