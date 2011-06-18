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

sys.argv[0] = os.environ.get('PYTHONSCRIPT', os.path.splitext(sys.executable)[0] +'.py')
__file__ = os.path.abspath(sys.argv[0])
execfile(__file__)
