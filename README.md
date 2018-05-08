![](fontstaller-logo.png)

A repo to install a few fav fonts in Linux environments

To install fonts in the directory `fonts` located in current directory to `~./fonts` run:

```bash
$ python3 fontstaller.py
```

It copies any font file containing folder to ~./fonts and extracts and font containg folder to ~./fonts. It also checks that there are no duplicates.

If you wist to install fonts to `\usr\share\fonts` You can use `--idir` option, but also take note that you would almost certainly have to use `sudo`.

### optional arguments

|  argument     | default     | description                                |
|  --------     | -------     | -----------                                |
|  -h, --help   |             | show help message and exit                 |
|  --fdir       | 'fonts'     | directory containing fonts                 |
|  --idir       | '~/.fonts'  | directory in which fonts will be installed |
|  --ignorezip  |             | Ignore zipped files                        |
