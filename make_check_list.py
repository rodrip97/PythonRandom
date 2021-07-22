import pandas as pd
import os
import warnings
from tkinter import Tk
from tkinter.filedialog import askopenfilename

warnings.simplefilter(action='ignore')
root = Tk()
root.withdraw()  # use to hide tkinter window

FILE_NAME = 'list_of_checks.xlsx'


def make_list():
    direct_deposit_path = askopenfilename(title="Direct Deposit", filetypes=[("Excel files", ".xlsx .xls")],
                                          initialdir='/')
    employees_file_path = askopenfilename(title="Today Employees", filetypes=[("Excel files", ".xlsx .xls")],
                                          initialdir='/')

    direct_deposit = pd.read_excel(direct_deposit_path, dtype={'Employee Number': 'int'}, engine='openpyxl')
    employees = pd.read_excel(employees_file_path, dtype={'EmployeeNumber ': 'int'}, engine='openpyxl')

    print(direct_deposit.dtypes)
    print(employees.dtypes)

    employees_data = employees[~employees['TimeIn'].isnull()]

    data = employees_data[~employees_data['EmployeeNumber'].isin(direct_deposit['Employee Number'])]
    data = data.sort_values(['Job Punched', 'LastFirst'])
    writer = pd.ExcelWriter(FILE_NAME, engine='openpyxl')
    data[['LastFirst', 'DateWorked', 'Job Punched', 'TimeIn']].to_excel(writer, index=False, sheet_name='report')


    writer.save()
    os.system(FILE_NAME)


make_list()
