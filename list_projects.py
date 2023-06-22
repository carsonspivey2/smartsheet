#!/usr/bin/env python3
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

# Get Workspace IDs
workspaces_response = client.Workspaces.list_workspaces(include_all=True)
# Extract id values
workspace_ids = [item.id for item in workspaces_response.data]
# Print sheets per workspace
for workspace_id in workspace_ids:
    workspace_response = client.Workspaces.get_workspace(workspace_id, load_all=True)
    # print('  ' + str(workspace_response.id) + '  ' + workspace_response.name)
    pcr_sheets = find_pcr_sheet(client, workspace_response, blacklist, pcr_sheets)

# End with counts
print ('\nTotal Workspaces: ' + str(len(workspace_ids)))
print('Total PCR Sheets: ' + str(len(pcr_sheets)))
