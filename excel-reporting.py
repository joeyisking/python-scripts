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
    Update_Month()
    Update_Report_Range(date)
    Update_Reported_Areas()
    wb.save('report.xlsm', as_template=False)

#Step 1 Import in the rows from the db based on date range
def Get_Date():
    end_date = input('Please enter the month you wish to run the report for dd/mm/YYYY')
    return end_date

#def Import_Data():

#Step 2 Recalculate totals
def Calculate_Totals(ws1, ws2):
    #There is a title row we dont want to include so set row to 2
    row = 2
     
    #Step 2.1 Total rows
    while ws1[row] != '':
        row++    
    ws2['B2'] = row
    
    #Step 2.2 Confirmed Reports
    for i in row:
#Step 2.3 Unconfirmed Reports
#Step 2.4 Fixed Reports
#Step 2.5 Check chart has been correctly updated

#Step 3 Update Report Month
#Step 4 Update Number of Reports per month
#Step 4.1 Check chart has been correctly updated
#Step 5 Get High Reported Areas

