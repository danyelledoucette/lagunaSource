from __future__ import print_function
from Google import Create_Service
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import pandas as pd
import numpy as np
import os.path

CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
gsheetId = "1W9IRnOpvTlHvmfydFs3SAWhmU1GwRI8PlzYuh62j8R8"

service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

def Export_Data_To_Sheets():
    URL = r'https://files.digital.nhs.uk/publicationimport/pub20xxx/pub20188/ccg-pres-data-oct-dec-2015-un-dat.csv'
    df = pd.read_csv(URL)
    df.replace(np.nan, '', inplace=True)

    response_date = service.spreadsheets().values().append(
        spreadsheetId=gsheetId,
        valueInputOption='RAW',
        range='DF1!A1',
        body=dict(
            majorDimension='ROWS',
            values=df.T.reset_index().T.values.tolist())
    ).execute()


    URL2 = r'https://raw.githubusercontent.com/franciscadias/data/master/kc_house_data.csv'
    df2 = pd.read_csv(URL2)
    df2.replace(np.nan, '', inplace=True)

    response_date = service.spreadsheets().values().append(
        spreadsheetId=gsheetId,
        valueInputOption='RAW',
        range='DF2!A1',
        body=dict(
            majorDimension='ROWS',
            values=df2.T.reset_index().T.values.tolist())
    ).execute()

Export_Data_To_Sheets()