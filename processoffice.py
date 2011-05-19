#!/usr/bin/env python
# coding:utf-8

import sys, os, re
import logging
import win32com.client
import comtypes, comtypes.client, comtypes.automation

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

def funcProcessExcelWorksheet(objWorksheet):
    '''http://www.okexcel.com.cn/bbs/viewthread.php?tid=26'''
    iRowCount = objWorksheet.UsedRange.Rows.Count
    #iRowCount = objWorksheet.Range("B65535").End(comtypes.gen.Excel.xlUp).Row
    lstValueCounts = []
    for iRow in range(1, iRowCount+1):
        strRange = 'A%d' % iRow
        objRange = objWorksheet.Range(strRange)
        logging.info('%s=%s', strRange, objRange.Value2)
    return True

def funcProcessExcelWorkbook(strFilename):
    try:
        logging.info('CreateObject Excel.Application')
        comtypes.client.GetModule(r'C:\Program Files\Microsoft Office\Office12\EXCEL.EXE')
        objApplication = comtypes.client.CreateObject('Excel.Application')
        #objApplication = win32com.client.DispatchEx('Excel.Application')

        logging.info('Open Workbook %r', strFilename)
        objWorkBook   = objApplication.Workbooks.Open(os.path.abspath(strFilename))
        for iCount in range(1, objWorkBook.Worksheets.Count+1):
            objWorksheet = objWorkBook.Worksheets(iCount)
            logging.info('Begin Process worksheet: %r', objWorksheet.Name)
            funcProcessExcelWorksheet(objWorksheet)
    except Exception, ex:
        logging.exception('funcProcessExcelWorkbook %r Error, %r', strFilename)
        raise
    finally:
        objWorkBook.Close(SaveChanges=1)
        objApplication.Quit()

def main():
    funcProcessExcelWorkbook(os.path.abspath(sys.argv[1]))

if __name__ == '__main__':
    main()

