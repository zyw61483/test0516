#! usr/bin/python3
import xlrd


def getColDate(filename):
	return getColDateBySICI(filename,0,0)

def getColDateBySICI(filename,sheetindex,colindex):
	book = xlrd.open_workbook(filename)
	sheet0 = book.sheet_by_index(sheetindex)
	return sheet0.col_values(colindex)