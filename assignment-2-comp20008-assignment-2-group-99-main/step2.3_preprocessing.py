import pandas as pd
# pip install xlrd==1.2.0
# pip install openpyxl

from math import isnan


# All functions are used to preprocessing the data. Filling the missing data with column average


# This function is used to filling a missing column by using the average of column before and after
def column_missing():
    excel = pd.read_excel('After/Y.xlsx')  # read excel
    private = pd.read_excel('After/Y.xlsx', 'Private')
    bed = pd.read_excel('After/Y.xlsx', 'Beds')

    name = list(excel.columns.values)

    for i in range(excel.shape[0]):  # iterate over rows for the first page of excel
        for j in range(excel.shape[1]):  # iterate over columns
            value = excel.at[i, name[j]]  # get cell value
            if not isinstance(value, str):  # value is not a string type
                if isnan(value):  # value is NaN
                    excel.at[i, name[j]] = ((excel.at[i, name[j - 1]] + excel.at[i, name[j + 1]]) / 2)
    excel.to_csv('After/Public_Hospital.csv')  # update
    private.to_csv('After/Private_Hospital.csv')
    bed.to_csv('After/Beds_Hospital.csv')

    return


# This function is used to filling the missing data by its column average
def row_missing():
    csv = pd.read_csv('After/Air.csv')  # read csv
    csv = csv.fillna(csv.mean())  # replace the NaN with column mean
    csv.to_csv('After/Air_Update.csv')  # update
    return


# Run function
column_missing()
row_missing()
