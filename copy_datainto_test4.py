#!/usr/bin/env python3
import configparser
import smartsheet

## \
### Inspiration from https://stackoverflow.com/questions/72650039
## /

config = configparser.ConfigParser()
config.read('config.ini')

# Read API key from config file
api_key = config.get('Smartsheet', 'API_KEY')

# Initialize Smartsheet client
client = smartsheet.Smartsheet(api_key)

# Read Smartsheet IDs from config file
template_smartsheet_id = config.get('Smartsheet', 'SOURCE_TEMPLATE_SMARTSHEET_ID')

# #grab all of the relevant sheets
# folder = client.Folders.get_folder(
#   ##################)       # folder_id of the project sheets
# for sheets in folder.sheets:
#     original_sheet_ids.append(str(sheets.id))
# print(original_sheet_ids)
# for index in range(len(original_sheet_ids)):
#     indexes.append(index)
# print(index)
original_sheet_ids = [
    int(config.get('Smartsheet', 'SOURCE_SMARTSHEET_TEST4_ID'))
]

#this function returns the last element in the new_sheet_ids
def linkup():
   return int(new_sheet_ids[-1])


def bigupdate():
    #loop through the process for each sheet, the 0:3 was for testing the first 3 sheets
    for original_sheet_id in original_sheet_ids#[0:3]:
        global new_sheet_ids
        new_sheet_ids = []
        global new_sheet_names
        new_sheet_names = []
        global pcr_sheet
        pcr_sheet = client.Sheets.get_sheet(
            int(original_sheet_id),
            include = 'all'
        )


        #make a copy of the template sheet were using for the update
        response1 = client.Sheets.copy_sheet(
            template_smartsheet_id,
            smartsheet.models.ContainerDestination({
                'destination_type': 'folder',               # folder, workspace, or home
                'destination_id': folderzeroid,         # folder_id of the new workspac - TODO (maybe use workspace instead of folder, and use `pcr_sheet.workspace.id`)
                'new_name': pcr_sheet.name
            }),
            include = ['rules','rulerecepients'],

        )
        print('creating a new sheet for: ' + pcr_sheet.name)
        time.sleep(1)

        #grab the folder of the new sheets, need to pull all those sheet ids
        folder2 = client.Folders.get_folder(
            ###################)       # folder_id of the new updates folder
        for sheets1 in folder2.sheets:
            new_sheet_ids.append(str(sheets1.id))
            new_sheet_names.append(str(sheets1.name))

        #here we iterate through to grab all the row ids from all the existing rows
        goodrow_ids = []
        for row in pcr_sheet.rows:
            if row.cells[0].value in testvalues:
                goodrow_ids.append(str(row.id))#,str(row.row_number)])
                print("another row prepped!")
        print(goodrow_ids)
        print('goodrow_ids printed!')

        result = linkup()
        print(result)
        #copy all the rows to the new sheet
        for  rowid in goodrow_ids:
            response = client.Sheets.copy_rows(
                int(original_sheet_id), #sheet id of row we are copying
                smartsheet.models.CopyOrMoveRowDirective({
                'row_ids' : int(rowid), #rowid of row to copy
                'to' : smartsheet.models.CopyOrMoveRowDestination({
                'sheet_id' : int(result)  #destination sheet id
                })
            }),
            include = ['all'], ignore_rows_not_found = True
            )
            print("rows loading in...")
        print(pcr_sheet.name + ' new sheet created!')
        sheetcounter + 1
        time.sleep(5)
bigupdate()
