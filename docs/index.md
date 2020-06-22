# HowDoI
#### Instant coding answers via the command line


Are you a hack programmer? Do you find yourself constantly Googling for how to do basic programming tasks?

Suppose you want to know how to format a date in bash. Why open your browser and read through blogs (risking major distraction) when you can simply stay in the console and ask howdoi:
```
$ howdoi format date bash
> DATE=`date +%Y-%m-%d`
```
HowDoI can answer all sorts of queries:
```python
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

$ howdoi convert mp4 to animated gif
> video=/path/to/video.avi
> outdir=/path/to/output.gif
> mplayer "$video" \
>         -ao null \
>         -ss "00:01:00" \  # starting point
>         -endpos 10 \ # duration in second
>         -vo gif89a:fps=13:output=$outdir \
>         -vf scale=240:180

$ howdoi create tar archive
> tar -cf backup.tar --exclude "www/subf3" www
```

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs help` - Print this help message.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
