"""
    FontStaller by @xypnox
    This script installs fonts for you
"""

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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Installs fonts in a given folder')
    parser.add_argument('--fdir',
                        default='fonts',
                        help='The directory containing fonts')
    parser.add_argument('--idir',
                        default=os.path.expanduser('~') + '/.fonts',
                        help='The directory in which fonts will be installed')
    parser.add_argument('--ignorezip',
                        action='store_true',
                        help='Ignore zipped files')
    args = parser.parse_args()

    print(args)

    fontdirs = []
    zipfiles = []

    for dirname, dirnames, filenames in os.walk(args.fdir):
        # print path to all subdirectories first.
        # for subdirname in dirnames:
        #     print(os.path.join(dirname, subdirname))

        # print path to all filenames.
        for filename in filenames:
            if isFont(filename):
                # print("Contains font", dirname)
                fontdirs.append(dirname)
            elif filename.endswith('zip'):
                zipfiles.append(os.path.join(dirname, filename))
            # print(os.path.join(dirname, filename))

        # Advanced usage:
        # editing the 'dirnames' list will stop os.walk() from recursing into there.
        if '.git' in dirnames:
            # don't go into any .git directories.
            dirnames.remove('.git')

    fontdirs = list(set(fontdirs))
    zipfiles = list(set(zipfiles))

    # print(fontdirs)
    # print(zipfiles)

    # Installs Fonts in fontdirs
    for dir in fontdirs:
        idir = args.idir + '/' + dir.split('/')[-1]
        if not os.path.exists(idir):
            os.makedirs(idir)
            onlyfiles = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f)) and not f.endswith('zip')]
            print(dir.split('/')[-1], onlyfiles)
            for file_ in onlyfiles:
                shutil.copy2(dir + '/' + file_, idir)
        else:
            print('Font Already Exists : ' + dir.split('/')[-1])

    for zfile in zipfiles:
        idir = args.idir + '/' + zfile.split('/')[-1][:-4]
        # print(idir)
        if not os.path.exists(idir):
            with ZipFile(zfile, 'r') as zipfile:
                for font in zipfile.namelist():
                    if isFont(font) is True:
                        zipfile.extractall(idir)
                        break
        else:
            print('Font Already Exisits : ' + zfile.split('/')[-1][:-4])
