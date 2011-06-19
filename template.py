#!/usr/bin/env python
# coding:utf-8

import sys, os, re, time
import logging
import glob

logging.basicConfig(level=0, format='%(levelname)s - - %(asctime)s %(message)s', datefmt='[%d/%b/%Y %H:%M:%S]')

def main():
    for filename in glob.glob(u'*'):
        logging.info(filename)

if __name__ == '__main__':
    main()

