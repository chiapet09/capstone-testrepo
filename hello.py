import openpyxl
import datetime
import os
from openpyxl import Workbook as book

workbook = book()
active_worksheet = workbook.active
active_worksheet['A1']= "Hello World"
active_worksheet['B1']= datetime.datetime.now()
workbook.save('test_workbook.xlsx')
print(os.listdir('.'))
