from googleapiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv
import json

import datetime

d = datetime.date.today()

CREDENTIALS_FILE = '../new_google_sheet/credentials.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])
service = discovery.build('sheets', 'v4', credentials=credentials)

dotenv_path = os.path.join(os.path.dirname(__file__), '../new_google_sheet/.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

spreadsheet_id = os.environ['SPREADSHEET_ID']

def get_sheets_artic(spreadsheet_id):
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id,
                                    range='H3:H27', majorDimension='ROWS').execute()
    values = result.get('values', [])
    range_update = 3

    with open('2022-05-27.json') as f:
        templates = json.load(f)

    for i in values:
        count = 0
        for j in i:
            for card in templates:
                if card['office_name'] != "Склад поставщика" and card['supplier_oper_name'] == 'Продажа' and card['nm_id']==int(j):
                    count += 1
        print (j,':',count)
    range_update = 3
    return
