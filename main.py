import sys
import os
import re
import xlrd
import xlwt
import datetime
import time

def run(filename):

	data_file = xlrd.open_workbook(filename)
	data_file_sheet = data_file.sheet_by_index(0)


	write_book = xlwt.Workbook()
	data_write_book = write_book.add_sheet('Results', cell_overwrite_ok=True)

	# Initialize a style
	value_names_style = xlwt.XFStyle()	 
	# Create a font
	font = xlwt.Font()
	font.name = 'Times New Roman'
	font.bold = True
	value_names_style.font = font

	debug = True
	separate_referenced_sections = True

	referenced_value_check = False
	fcs_section_check = False
	# ASSIGN VARIABLES
	fcs_section_number = 0
	fcs_section_auto_number = 1
	referenced_value = 0
	section_abs_number = 0
	final_abs_number = 0
	save_value_title = False
	sheet_row = 0
	sheet_column = 0

	for rownum in range(data_file_sheet.nrows):

		row_column = 1

		for b in range(len(data_file_sheet.row_values(rownum))):
			value = str(data_file_sheet.row_values(rownum)[b])
			
			# Check for Depth in 1. column and search for reference value
			if row_column is 1:
				depth_step = value.count('>')
				if debug is True:
					print "DEBUG: == depth_step =="
					print depth_step
				
				if depth_step is 4:
					referenced_value_check = True
					if separate_referenced_sections is True:
						sheet_column += 1
					if debug is True:
						print "DEBUG: == referenced_value_check is TRUE =="
				else:
					referenced_value_check = False
					if debug is True:
						print "DEBUG: == referenced_value_check is FALSE =="

				if depth_step is 0 and len(value) is 0:
					fcs_section_check = True
					fcs_section_auto_number += 1
				else:
					fcs_section_check = False


			if referenced_value_check is True and row_column is 2:
				if separate_referenced_sections is True:
					sep_style = xlwt.easyxf('font: bold 1, color red;')
					data_write_book.write(sheet_row, sheet_column, value, sep_style)

			if referenced_value_check is True and row_column is 3:
				referenced_value = num(value)

				if debug is True:
					print "DEBUG: == referenced_value =="
					print value

				if referenced_value is not 0 and fcs_section_number is not 0:
					section_abs_number = (referenced_value / 100) * num(fcs_section_number)

			if fcs_section_check is True and row_column is 2:

				# fcs_section_number = raw_input('Please enter value for '+ value +'? ')

				# Automatic take value from excel file

				fcs_section_number = automatic_fcs_section_number(filename, fcs_section_auto_number)

				if debug is True:
					print "DEBUG: == fcs_section_auto_number =="
					print fcs_section_auto_number
					print "DEBUG: == referenced_value =="
					print referenced_value
					print "DEBUG: == fcs_section_number =="
					print fcs_section_number				

				sheet_row += 1
				sheet_column = 0

				# Write section name
				data_write_book.write(sheet_row, sheet_column, value)

			if row_column is 1:
				depth_step = value.count('>')
				if depth_step is 5:
					save_value_title = True
					sheet_column += 1
				else:
					save_value_title = False

			if referenced_value_check is True and row_column is 3:

				final_abs_number = (num(value) / 100) * num(fcs_section_number)

				if debug is True:
					print "VALUE: ", value
					print "SECTION ABS NUMBER: ", fcs_section_number
					print "REF VALUE ABS: ", final_abs_number

				sheet_column += 1
				data_write_book.write(sheet_row, sheet_column, num(value))

				sheet_column += 1
				data_write_book.write(sheet_row, sheet_column, final_abs_number)


			if save_value_title is True and row_column is 2:
				print value
				data_write_book.write(sheet_row, sheet_column, value, value_names_style)

			if save_value_title is True and row_column is 3:
				print value
				sheet_column += 1
				data_write_book.write(sheet_row, sheet_column, num(value))

				sheet_column += 1
				final_abs_number = (num(value) / 100) * section_abs_number
				data_write_book.write(sheet_row, sheet_column, final_abs_number)
				if debug is True:
					print "DEBUG: == VALUE:  =="
					print num(value)
					print "DEBUG: == section_abs_number:  =="
					print section_abs_number


			# if save_value_title is True and row_column is 4:
			# 	sheet_column += 1
			# 	data_write_book.write(sheet_row, sheet_column, value)

			row_column += 1

	write_book.save(file_name(filename + " - "))	


def automatic_fcs_section_number(filename, automatic_fcs_section_number):
	data_file = xlrd.open_workbook("Sections_input.xls")
	data_file_sheet = data_file.sheet_by_index(0)
	print "DEBUG: == automatic_fcs_section_number == ", automatic_fcs_section_number
	cell = data_file_sheet.cell(automatic_fcs_section_number-1,find_val_in_workbook(filename))

	cell_value = cell.value.split()

	final_cell_value = num(cell_value[0]) * (10 ** num(cell_value[1]))
	print "DEBUG: == cell_value == ", final_cell_value


	return num(final_cell_value)


def find_val_in_workbook(val):
	data_file = xlrd.open_workbook("Sections_input.xls")
	data_file_sheet = data_file.sheet_by_index(0)

	for rownum in range(data_file_sheet.nrows):
		row_column = 1
		for b in range(len(data_file_sheet.row_values(rownum))):
			value = str(data_file_sheet.row_values(rownum)[b])
			if value == val:
				return row_column-1

			row_column += 1

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def file_name(start_s):
	f_name = datetime.datetime.now()
	f_name = f_name.strftime(start_s + "_%B_%d_%Y_%I_%M%p.xls")
	return f_name

if __name__ == '__main__':
	os.chdir("./data")
	files = []
	for filename in os.listdir("."):
	    if filename.endswith(".xls") and filename != "Sections_input.xls":
	    	files.append(filename)
	    	run(filename)