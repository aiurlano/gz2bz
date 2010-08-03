#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, gzip, bz2, traceback

if __name__ == "__main__":
    if len(sys.argv)<2:
        print "\nUsage: "+sys.argv[0]+" <filename>\n\n   converts the file name from gzip to bzip2.\n   Note that filename must end with .gz"
        exit(1)

    if not sys.argv[1].endswith(".gz"):
        print "\nUsage: "+sys.argv[0]+" <filename>\n\n   converts the file name from gzip to bzip2.\n   Note that filename must end with .gz"
        exit()

    basefilename=sys.argv[1][:-3]
    print basefilename
    try:
        ifd = gzip.GzipFile(filename=basefilename+".gz", mode='rb')
        ofd = bz2.BZ2File(filename=basefilename+".bz2", mode='wb', compresslevel=9)
        while True:
            buffer=ifd.read(20480)
            if buffer:
                ofd.write(buffer)
            else:
                break
    except (Exception), why:
        print "There was an error: ", why
    sys.exit(0)
    

