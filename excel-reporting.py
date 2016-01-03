#== Installation ==
# May need to pull in db connector
# Must have openpyxl installed to edit the xlsx file
# $ pip install openpyxl
from openpyxl import Workbook

def main():
    date = Get_Date()

    #load the base xlsx file
    wb = load_workbook('report.xlsx')
    ws1 = wb.get_sheet_by_name("Sheet 1")
    ws2 = wb.get_sheet_by_name("Sheet 2")
    #ws2 = Import_Data(ws2, date)
    ws1 = Calculate_Totals(ws1, ws2)
    ws1 = Update_Month(date, ws1)
    ws1 = Update_Report_Range(date, ws1)
    ws1 = Update_Reported_Areas(ws1, ws2)
    wb.save('report.xlsm', as_template=False)

#Step 1 Import in the rows from the db based on date range
def Get_Date():
    end_date = input('Please enter the month you wish to run the report for dd/mm/YYYY')
    return end_date

#def Import_Data():

#Step 2 Recalculate totals
def Calculate_Totals(ws1, ws2):
    #There is a title row we dont want to include so set row to 2
    rows = 2
    confirmed = 0
    unconfirmed = 0
    fixed = 0

    #Step 2.1 Total rows
    while ws2['A' + rows] != '':
        rows++    
    
    ws1['B2'] = row
    
    for row in rows:
        #Step 2.2 Confirmed Reports
        if ws2['P' + row] == 'confirmed':
            confirmed += 1
        #Step 2.3 Unconfirmed Reports
        elif ws2['P' + row] == 'unconfirmed':
            unconfirmed += 1
        #Step 2.4 Fixed Reports
        elif ws2['P' + row] == 'fixed - user':
            fixed += 1
        else: exit('unknown type of state')

    ws1['B3'] = confirmed
    ws1['B4'] = unconfirmed
    ws1['B5'] = fixed
    
    #Step 2.5 Will need to manually check chart has been correctly updated
    return ws1

#Step 3 Update Report Month
def Update_Month(date, ws1):
 
#Step 4 Update Number of Reports per month
def Update_Report_Range(ws1):
#Step 4.1 Check chart has been correctly updated
#Step 5 Get High Reported Areas

