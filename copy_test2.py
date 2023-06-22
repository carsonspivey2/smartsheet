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
template_smartsheet_id = config.get('Smartsheet', 'SOURCE_TEMPLATE_SMARTSHEET_ID')
test_smartsheet_id = config.get('Smartsheet', 'SOURCE_SMARTSHEET_TEST2_ID')

# Get sheets
template_sheet = client.Sheets.get_sheet(template_smartsheet_id)
test_sheet = client.Sheets.get_sheet(test_smartsheet_id)

# Append template data
print('Updating Test Sheet 2: ID ' + test_smartsheet_id)
#   Columns - check first, then add
if not find_pcrid_column(test_sheet.columns)
    print('  Adding ' + str(template_sheet.columns) + ' new columns')
    test_sheet.columns.append(template_sheet.columns)
else:
    print('  Not adding columns - "PCR ID" exists')
# Rows - add all to end
print('  Adding ' + str(template_sheet.row) + ' new rows')
test_sheet.rows.append(template_sheet.rows)

# Replace the sheet with the newly appended data and save it
client.Sheets.update_sheet(target_sheet_id, sheet=smartsheet.models.Sheet(automation=automation))
print('\nAutomation section data mirroring complete - please verify')
