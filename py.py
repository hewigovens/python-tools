#!/usr/bin/env python
# coding:utf-8

import psyco
psyco.full()

import sys, os
sys.path += ['.', os.path.dirname(sys.executable)]

import sys, os, re, time, inspect, errno, copy
import logging, logging.handlers, logging.config
import cStringIO, StringIO, string, types, weakref
import tarfile, zipfile, tempfile
import glob, shutil, hashlib, json, platform, random, uuid
import base64, binascii, cgi, ConfigParser, csv, fnmatch, optparse, urlparse
import xml, xml.dom, xml.dom.minidom
import lxml.etree, lxml._elementpath, gzip
import sqlite3, bsddb
import socket, ssl, thread, select, asyncore
import BaseHTTPServer, SocketServer, CGIHTTPServer
import httplib, urllib, urllib2, ftplib, telnetlib, smtplib, socks
import email.iterators, email.Iterators, email.Utils, email.base64MIME, email.mime.text
import OpenSSL, Crypto.Cipher.AES
import ctypes, ctypes.wintypes, comtypes, comtypes.client
import win32api, win32process, win32con, win32gui, win32com.client, wmi

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