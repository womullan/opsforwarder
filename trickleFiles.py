#!/usr/bin/env python3

"""
Given a two directories periodically copy a file from one to the other
simulating arrival of images from the telescope .
Hence there may be some order to be respected ...
womullan 2019
"""

import os
import time
import argparse


def doCopy(inDir, outDir, interval, verbose):
    """For all files in inDir  scp  them to out dir
    not preserving any directory structure.
    Pause interval seconds between files
    Assumes ssh keys are in place so it can do SCP

    Parameters
    ----------
    inDir : `str`
       directory with files to copy
    outDir : `str`
       remote locaiton  e.g. user@host:directory

    """
    count = 0
    if not interval:
        interval = 5
    if verbose:
        print("from {} to {} with {} s".format(inDir, outDir, interval))
    filelist = os.listdir(inDir)
    for fn in filelist:
        scpCmd = 'scp {} {}'.format(fn, outDir)
        count = count + 1
        if verbose:
            print(str(scpCmd))
            print('Sleeping {} second'.format(interval))
        time.sleep(interval)
    # End doCopy


if __name__ == "__main__":
    description = __doc__
    formatter = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(description=description,
                                     formatter_class=formatter)

    parser.add_argument('inDir', help='inputDirectory to process')
    parser.add_argument('outDir', help='outDirectory form user@host:dir')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help=' Print anoying messages ')
    parser.add_argument('-i', '--interval', type=int,
                        help='Seconds between transfers ')

    args = parser.parse_args()
    doCopy(args.inDir, args.outDir, args.interval, args.verbose)
