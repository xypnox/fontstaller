from zipfile import ZipFile
import argparse
import shutil
import os


def isFont(arg):
    if arg.endswith('ttf'):
        return True
    elif arg.endswith('otf'):
        return True
    return False


class Fontstaller:
    def __init__(self, dir):
        self.dir = dir

    def install(self, exdir):
        with ZipFile(self.dir, 'r') as myzip:
            myzip.extract(exdir)

    def checkFont(self):
        with ZipFile(self.dir, 'r') as myzip:
            for font in myzip.namelist():
                if isFont(font) is True:
                    return True

        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Installs fonts in a given folder')
    parser.add_argument('--fdir',
                        default='fonts',
                        help='The directory containing fonts')
    parser.add_argument('--idir',
                        default='~./fonts',
                        help='The directory in which fonts will be installed')
    parser.add_argument('--ignorezip',
                        action='store_true',
                        help='Ignore zipped files')
    args = parser.parse_args()

    fontdirs = []

    for dirname, dirnames, filenames in os.walk(args.fdir):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            print(os.path.join(dirname, subdirname))

        # print path to all filenames.
        for filename in filenames:
            if isFont(filename):
                print("Contains font", dirname)
            print(os.path.join(dirname, filename))

        # Advanced usage:
        # editing the 'dirnames' list will stop os.walk() from recursing into there.
        if '.git' in dirnames:
            # don't go into any .git directories.
            dirnames.remove('.git')
