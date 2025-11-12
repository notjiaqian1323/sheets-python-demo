import gspread 
import os

# Use os.path.join and os.path.dirname(__file__) 
# to ensure the script finds the file relative to its own location.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_FILE = os.path.join(BASE_DIR, 'credentials.json')

gc = gspread.service_account(filename=CREDENTIALS_FILE)
sh = gc.open_by_key('1v8H2zbmUnyMZor2T_OjQp8S-823wbcSEXrmN3zEPFSc')
worksheet = sh.sheet1

#get all data from th spreadsheet
#res = worksheet.get_all_records() #returns a list of dictionaries
res2 = worksheet.get_all_values() #returns a list of lists
res3 = worksheet.row_values(1) #returns the ultimate first row, that is the column names
res4 = worksheet.col_values(1) #returns the values of the first column

#get individual values
res5 = worksheet.get('A2') #specific cell number
res6 = worksheet.get('A2:C2') #accessing a range of values

#add cell
user = ["Susan", 25, "Sydney"]
#worksheet.insert_row(user, 3) #insert this row at position of 3k
#worksheet.append_row(user) #auto add to last row

#update cell
worksheet.update_cell(6,2, 28) #row num, col num

#delete cells
worksheet.delete_rows(1)


#print(res)
#print(res2)
print(res3)
print(res4)
print(res5)
