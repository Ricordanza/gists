# -*- coding:utf-8 -*-

import sys
import codecs

def main():
    arg = sys.argv

    with codecs.open(arg[1], "r", "shift_jis") as rfile:

        lines = rfile.readlines()
        rlines = [l for l in lines if arg[2] in l]

        for line in rlines:
            print line.rstrip()

        if len(arg) > 3:
            with codecs.open(arg[3], "w", "shift_jis") as wfile:
                for line in rlines:
                    wfile.write(line)

    sys.exit(0)

if __name__ == '__main__':
    main()