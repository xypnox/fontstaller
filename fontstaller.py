from zipfile import ZipFile


class Fontstaller:
    def __init__(self, dir='.', exdir='~/.fonts'):
        self.dir = dir
        self.exdir = exdir

    def install(self):
        with ZipFile(self.dir, 'r') as myzip:
            myzip.extract(self.exdir)

    def checkFont(self):
        with ZipFile(self.dir, 'r') as myzip:
            for font in myzip.namelist():
                if font.endswith('ttf'):
                    return True
                elif font.endswith('otf'):
                    return True
        return False
