# coding: utf-8
import os
import glob
import codecs
import xlwt # Excel library from http://www.python-excel.org/
from optparse import OptionParser
import xml.dom.minidom

def getOptions():
	parser = OptionParser()
	parser.add_option("-d", "--directory", help="Android project root directory.", metavar=FILE)
	parser.add_option("-o", "--output", help="Output excel file.")
	return parser.parse_args()

def getNodeValue(node):
	value = ''
	if node.firstChild:
		value = node.firstChild.nodeValue

	return value

def getNodeKey(node):
	return node.attributes['name'].value

def getNodeValueByKey(nodes, key):
	for node in nodes:
		if getNodeKey(node) == key:
			return getNodeValue(node)
	return ''

def getNodeList(xmlFile):
	xmldoc = xml.dom.minidom.parse(xmlFile)
	return xmldoc.getElementsByTagName('string') 

def initWorkBook():
	return xlwt.Workbook(encoding='utf-8')

def getSheet(book):
	return book.add_sheet('Android localization', cell_overwrite_ok=True)

def saveWorkBook(book, fileName):
	book.save(fileName)

def writeMasterKeys(sheet, nodes):
	sheet.write(0, 0, 'keys')

	row = 1
	for node in nodes:
		sheet.write(row, 0, getNodeKey(node))
		row += 1

def writeMasterValues(sheet, nodes):
	row = 1
	for node in nodes:
		sheet.write(row, 1, getNodeValue(node))
		row += 1

def writeValues(sheet, masterNodeList, nodes, col):
	row = 1
	for node in masterNodeList:
		key = getNodeKey(node)
		value = getNodeValueByKey(nodes, key)
		sheet.write(row, col, value)
		row += 1

def writeNodesToColumn(sheet, masterNodeList, nodes, langCode, col):
	sheet.write(0, col, langCode)
	writeValues(sheet, masterNodeList, nodes, col)

def writeMasterNodeList(sheet, nodes):
	writeMasterKeys(sheet, nodes)
	writeMasterValues(sheet, nodes)

def getStringsXmlFiles(directory):
	return glob.glob(os.path.join(options.directory, 'res/values-*/strings.xml'))

def getMasterNodeList(directory):
	xmlFile = glob.glob(os.path.join(options.directory, 'res/values/strings.xml'))[0]
	return getNodeList(xmlFile)

def getLangCode(xmlFile):
	(head, tail) = os.path.split(xmlFile)
	(head, tail) = os.path.split(head)
	return tail.replace('values-', '')

if __name__ == '__main__':
	(options, args) = getOptions()

	book = initWorkBook()
	sheet = getSheet(book)
	
	masterNodeList = getMasterNodeList(options.directory)
	writeMasterNodeList(sheet, masterNodeList)

	i = 2
	for xmlFile in getStringsXmlFiles(options.directory):
		langCode = getLangCode(xmlFile)
		nodes = getNodeList(xmlFile)
		writeNodesToColumn(sheet, masterNodeList, nodes, langCode, i)
		i += 1

	saveWorkBook(book, options.output)