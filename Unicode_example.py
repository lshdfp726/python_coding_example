#! /usr/bin/env python
# -*- coding:UTF-8 -*-

'test Chinese character encoding'

CODEC = 'utf-8'
FILE = 'unicode.txt'


def writeToFile(params):
	str = params
	outPutStr = str.encode(CODEC)
	f = open(FILE,'w')
	f.write(outPutStr)
	f.close()


def readFromFile():
	f = open(FILE,'r')
	inOutStr = f.read()
	f.close()
	str = inOutStr.decode(CODEC)
	print str


if __name__ == '__main__':
	writeToFile(u'中华人民共和国')
	readFromFile()
