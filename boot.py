#!/usr/bin/env python
# coding:utf-8

import sys, os
sys.dont_write_bytecode = True
sys.path += ['.', os.path.dirname(getattr(sys, 'executable', sys.argv[0]))]

import sys, os, re, time
import errno, zlib, struct, binascii
import logging
import httplib, urllib2, urlparse, socket, select
import BaseHTTPServer, SocketServer
import ConfigParser
import ssl
import ctypes
import threading, Queue
import OpenSSL

if 'PYTHONSCRIPT' in os.environ and not os.path.exists(os.environ['PYTHONSCRIPT']):
    exec(os.environ['PYTHONSCRIPT'])
else:
    __file__ = sys.argv[0] = os.path.abspath(os.environ.get('PYTHONSCRIPT', os.path.splitext(sys.executable)[0] +'.py'))
    execfile(__file__)
