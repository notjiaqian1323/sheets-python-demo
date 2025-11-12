import gspread 

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1v8H2zbmUnyMZor2T_OjQp8S-823wbcSEXrmN3zEPFSc')
worksheet = sh.sheet1

#get all data from th spreadsheet
res = worksheet.get_all_records()