#!/usr/bin/env python
# coding:utf-8

import sys, os
sys.path += ['.', os.path.dirname(sys.executable)]

import os, sys, re
import glob

if os.path.splitext(sys.argv[0])[1] == '':
    sys.argv[0] += '.exe'
if sys.executable == os.path.abspath(sys.argv[0]):
    sys.argv[0] = os.path.splitext(sys.executable)[0] +'.py'
    if os.path.isfile(sys.argv[0]):
        __file__ = sys.argv[0]
        execfile(sys.argv[0])
    else:
        sys.stderr.write('%r is not exists.\n' % sys.argv[0])
else:
    sys.stderr.write('Error: %r != %r\n' % (sys.executable, sys.argv[0]))
