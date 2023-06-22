#!/usr/bin/env python3
from collections.abc import Iterable
# from utils.find_pcrid_column import find_pcrid_column

def find_pcr_sheet(client, workspace, blacklist, collection):
    if workspace.sheets:
        for sheet in workspace.sheets:
            # if sheet.id in blacklist:
            #     print('BLACKLISTED ' + str(sheet.id))
            if sheet.id not in blacklist and 'PCR' in sheet.name:
                # print('    sheet: ' + str(sheet.id) + '  ' + sheet.name)
                # full_sheet = client.Sheets.get_sheet(sheet.id)
                # if not find_pcrid_column(full_sheet.columns):
                collection.append(sheet)
    # Recurse into nested "folders" searching for sheets
    if workspace.folders and isinstance(workspace.folders, Iterable):
        for folder in workspace.folders:
            collection = find_pcr_sheet(client, folder, blacklist, collection)
    # Return the counter after everything is parsed
    return collection
