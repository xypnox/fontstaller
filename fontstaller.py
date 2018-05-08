from zipfile import ZipFile
import argparse


class Fontstaller:
    def __init__(self, dir):
        self.dir = dir

    def install(self, exdir):
        with ZipFile(self.dir, 'r') as myzip:
            myzip.extract(exdir)

    def checkFont(self):
        with ZipFile(self.dir, 'r') as myzip:
            for font in myzip.namelist():
                if font.endswith('ttf'):
                    return True
                elif font.endswith('otf'):
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
