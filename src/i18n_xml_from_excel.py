# coding: utf-8
import os
import codecs
import xlrd # Excel library from http://www.python-excel.org/
from optparse import OptionParser

def createAndInitXmlFile(languageCode):
	directory = 'res/values'

	if languageCode:
		directory = '%s-%s'%(directory, languageCode)

	if not os.path.exists(directory):
		os.makedirs(directory)

	xmlFile = codecs.open(directory + '/strings.xml', 'w+', encoding='utf-8')
	xmlFile.write('<?xml version="1.0" encoding="utf-8" standalone="no"?>\n')
	xmlFile.write('<resources>\n')

	return xmlFile

def endAndCloseXmlFile(xmlFile):
	xmlFile.write('</resources>\n')
	xmlFile.close()

def getCleanString(input):
	input = input.replace('\ ', ' ')
	input = input.replace('...', '&#8230;')
	input = input.replace(u'…', '&#8230;')
	input = input.replace('"', '\"')
	
	# write here any usual replace that you need to perform
	
	return input

def getXmlString(key, value):
	if key:
		return '<string name="%s">%s</string>\n'%(key, value)
	else:
		if value:
			print 'WARNING! EMPTY KEY WITH NOT EMPTY VALUE "%s". EXCEL CAN BE BAD FORMATTED'

		return ''

def getCellTextValue(row, column):
	cellType = sheet.cell_type(row, column)
	cellValue = sheet.cell_value(row, column)
	
	if cellType in (2,3) and int(cellValue) == cellValue:
		cellValue = int(cellValue)

	return '%s'%(cellValue)

if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option("-f", "--file", help="Input Excel file.", metavar="FILE")
	parser.add_option("-c", "--clean", help="Use this option to clean strings and leave XMLs Android Lint proof.", action="store_true", default=False)

	(options, args) = parser.parse_args()

	sheet = xlrd.open_workbook(options.file).sheet_by_index(0)
	
	for column in range(1, sheet.ncols):
		xmlFile = createAndInitXmlFile(sheet.cell_value(0, column))
		
		for row in range(1, sheet.nrows):
			cellValue = getCellTextValue(row, column)
			
			if options.clean:
				cellValue = getCleanString(cellValue)	

			xmlFile.write(getXmlString(sheet.cell_value(row, 0), cellValue))
	
		endAndCloseXmlFile(xmlFile)