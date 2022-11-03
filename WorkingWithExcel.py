import xlwt
from xlwt import Workbook

wb = Workbook()

sheet_1 = wb.add_sheet('Sheet_1')

sheet_1.write(1, 0, 'Random String')

wb.save('xlwt example.xls')




'''
import xlsxwriter
wb = xlsxwriter.Workbook('hello.xlsx')
worksheet = wb.add_worksheet()
worksheet.write('A1', 'Hello')
wb.close()
'''
