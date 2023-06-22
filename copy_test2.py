import configparser
import smartsheet
from utils.find_pcr_sheet import find_pcr_sheet
from utils.find_pcrid_column import find_pcrid_column

config = configparser.ConfigParser()
config.read('config.ini')

# Read API key from config file
api_key = config.get('Smartsheet', 'API_KEY')

# Initialize Smartsheet client
client = smartsheet.Smartsheet(api_key)

# Read Smartsheet IDs from config file
template_smartsheet_id = config.get('Smartsheet', 'SOURCE_SMARTSHEET_TEMPLATE_ID')
test_smartsheet_id = config.get('Smartsheet', 'SOURCE_SMARTSHEET_TEST2_ID')

# Get sheets
template_sheet = client.Sheets.get_sheet(template_smartsheet_id)
test_sheet = client.Sheets.get_sheet(test_smartsheet_id)

# Append template data
print('Updating Test Sheet 2: ID ' + test_smartsheet_id)
#   Columns - check first, then add
hasPrcColumns = find_pcrid_column(test_sheet.columns)
if not hasattr(test_sheet, 'columns') and not hasPrcColumns:
    test_sheet.columns = [] # If we need to add colunms and no prop/collection, add it (then append)
if not hasPrcColumns:
    print('  Adding new columns') #print('  Adding ' + str(template_sheet.columns) + ' new columns')
    test_sheet.columns.append(template_sheet.columns)
else:
    print('  Not adding columns - "PCR ID" exists')
# Rows - add all to end
print('  Adding new rows') #print('  Adding ' + str(template_sheet.row) + ' new rows')
if not hasattr(test_sheet, 'rows'):
    test_sheet.columns = [] # If no rows prop/collection, add it (then append)
test_sheet.rows.append(template_sheet.rows)

# Replace the sheet with the newly appended data and save it
client.Sheets.update_sheet(test_smartsheet_id, smartsheet.models.Sheet(test_sheet))
print('\nAutomation section data mirroring complete - please verify')
