import configparser
import smartsheet

config = configparser.ConfigParser()
config.read('config.ini')

# Read API key from config file
api_key = config.get('Smartsheet', 'API_KEY')

# Initialize Smartsheet client
client = smartsheet.Smartsheet(api_key)

# Read Smartsheet ID from config file
smartsheet_id = config.get('Smartsheet', 'SOURCE_SMARTSHEET_TEST3_ID')

# Get Template
sheet = client.Sheets.get_sheet(smartsheet_id)
print(sheet)
