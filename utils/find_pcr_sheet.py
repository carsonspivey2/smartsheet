from collections.abc import Iterable
# from utils.find_prcid_column import find_prcid_column

def find_pcr_sheet(workspace, blacklist, collection):
    if workspace.sheets:
        for sheet in workspace.sheets:
            # if sheet.id in blacklist:
            #     print('BLACKLISTED ' + str(sheet.id))
            if sheet.id not in blacklist and 'PCR' in sheet.name:#sheet.name.startswith('PCRs - '):# and find_prcid_column(sheet.columns):
                collection.append(sheet)
                # print('    sheet: ' + str(sheet.id) + '  ' + sheet.name)
                # full_sheet = client.Sheets.get_sheet(sheet.id)
                # print(full_sheet)
                # print('\n')
    # Recurse into nested "folders" searching for sheets
    if workspace.folders and isinstance(workspace.folders, Iterable):
        for folder in workspace.folders:
            collection = find_pcr_sheet(folder, blacklist, collection)
    # Return the counter after everything is parsed
    return collection
