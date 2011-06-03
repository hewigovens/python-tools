#!/usr/bin/env python
# coding:utf-8

import psyco
psyco.full()

import sys, os
sys.path += ['.', os.path.dirname(sys.executable)]

import sys, os, re, time
import errno, zlib, struct, logging
import httplib, urllib2, urlparse, socket, select
import BaseHTTPServer, SocketServer
import threading, Queue
import ConfigParser
import ssl
import ctypes
import OpenSSL.crypto


sys.argv.pop(0)
if sys.argv[0] == '-c':
    sys.argv.pop(0)
    exec(sys.argv[0])
elif os.path.isfile(sys.argv[0]):
    sys.argv[0] = os.path.abspath(sys.argv[0])
    __file__ = sys.argv[0]
    execfile(sys.argv[0])
else:
    raise RuntimeError(u'Unkown command %r' % sys.argv)