# fontstaller
A repo to install a few fav fonts in Linux environments

To install fonts in the directory `fonts` located in current directory to `~./fonts` run:

```bash
$ python3 fontstaller.py
```

### optional arguments

|  argument     | default     | description                                |
|  --------     | -------     | -----------                                |
|  -h, --help   |             | show help message and exit                 |
|  --fdir       | 'fonts'     | directory containing fonts                 |
|  --idir       | '~/.fonts'  | directory in which fonts will be installed |
|  --ignorezip  |             | Ignore zipped files                        |
