import configparser
import smartsheet
from utils.find_pcr_sheet import find_pcr_sheet

config = configparser.ConfigParser()
config.read('config.ini')

# Read API key from config file
api_key = config.get('Smartsheet', 'API_KEY')

# Do not use test-sheets
blacklist = [
    int(config.get('Smartsheet', 'SOURCE_SMARTSHEET_TEST1_ID')),
    int(config.get('Smartsheet', 'SOURCE_SMARTSHEET_TEST2_ID'))
]

pcr_sheets = [] # Collection of PCR Sheets

# Initialize Smartsheet client
client = smartsheet.Smartsheet(api_key)

# Read Smartsheet IDs from config file
template_smartsheet_id = config.get('Smartsheet', 'SOURCE_TEMPLATE_SMARTSHEET_ID')

# Get template sheet
template_sheet = client.Sheets.get_sheet(template_smartsheet_id)

# Get Workspace IDs
workspaces_response = client.Workspaces.list_workspaces(include_all=True)
# Extract id values
workspace_ids = [item.id for item in workspaces_response.data]
# Print sheets per workspace
for workspace_id in workspace_ids:
    workspace_response = client.Workspaces.get_workspace(workspace_id, load_all=True)
    # print('  ' + str(workspace_response.id) + '  ' + workspace_response.name)
    pcr_sheets = find_pcr_sheet(workspace_response, blacklist, pcr_sheets)

# Update each sheet
for pcr_sheet in pcr_sheets
# Append template data
    print('Updating ' + pcr_sheet.id)
    #   Columns - check first, then add
    if not find_pcrid_column(pcr_sheet.columns)
        print('  Adding ' + str(template_sheet.columns) + ' new columns')
        pcr_sheet.columns.append(template_sheet.columns)
    else:
        print('  Not adding columns - "PCR ID" exists')
    # Rows - add all to end
    print('  Adding ' + str(template_sheet.row) + ' new rows')
    pcr_sheet.rows.append(template_sheet.rows)
    # Replace the sheet with the newly appended data and save it
    client.Sheets.update_sheet(target_sheet_id, sheet=smartsheet.models.Sheet(automation=automation))
    print('\n')

print('\nAutomation section data mirroring complete')
