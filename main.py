import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope=['https://spreadsheets.google.com/feeds']
client_secret_file='client_secret.json'
creds=ServiceAccountCredentials.from_json_keyfile_name(client_secret_file,scope)
client=gspread.authorize(creds)
sheet=client.open('Legislators 2017').sheet1
legislators=sheet.get_all_records()

pp=pprint.PrettyPrinter()
row=sheet.row_values(6)
col=sheet.col_values(6)
result=sheet.cell(6,11).value
sheet.update_cell(6,11,'555-867-5309')
row_text=["I'm","updating","a","spreadsheet","from","python"]
index=3
sheet.insert_row(row,index)
sheet.delete_row(3)
