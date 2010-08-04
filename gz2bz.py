#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, gzip, bz2, traceback

def printUsage():
    print "\nUsage: "+sys.argv[0]+" <filename>\n\n  Converts <filename> from gzip to bzip2.\n  Note that <filename> must end with .gz"
    

if __name__ == "__main__":
    if (len(sys.argv)<2) or (not sys.argv[1].endswith(".gz")):
        printUsage()
        exit(1)

    basefilename=sys.argv[1][:-3]
    print basefilename,":",
    if os.path.exists(basefilename+".bz2"):
        print "Error: "+basefilename+".bz2 already exists. Exiting"
        exit(2)

    try:
        ifd = gzip.GzipFile(filename=basefilename+".gz", mode='rb')
        ofd = bz2.BZ2File(filename=basefilename+".bz2", mode='wb', compresslevel=9)
        while True:
            buffer=ifd.read(20480)
            if buffer:
                ofd.write(buffer)
            else:
                break
        print "OK"
    except (Exception), why:
        print "Error", why

    sys.exit(0)
    

