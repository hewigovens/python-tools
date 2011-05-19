#!/usr/bin/env python
# coding:utf-8

import sys, os, re, time
import logging
import glob

logging.basicConfig(level=0, format='%(asctime)s %(levelname)s %(message)s')

def main():
    for strFilename in glob.glob('*'):
        logging.info(strFilename)

if __name__ == '__main__':
    main()

