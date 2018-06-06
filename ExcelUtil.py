#! usr/bin/python3
import xlrd

def _getSheet(filename,sheetindex):
	book = xlrd.open_workbook(filename)
	return book.sheet_by_index(sheetindex)

def getColDate(filename):
	return getColDateBySICI(filename,0,0)

def getColDateBySICI(filename,sheetindex,colindex):
	sheet = _getSheet(filename,sheetindex)
	return sheet.col_values(colindex)
	
def getFromFirstRow(filename,sheetindex):
	return get(filename,sheetindex,0)
	
def get(filename,sheetindex,rowIndex):
	sheet = _getSheet(filename,sheetindex)
	dict = {}
	for row in range(rowIndex,sheet.nrows):
		list = []
		for col in range(sheet.ncols):
			val = sheet.cell(row,col).value
			list.append(val)
			# print(val,end=' ')
		# print()
		dict[row]=list
	return dict