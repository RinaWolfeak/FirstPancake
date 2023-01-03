import requests
import json
from flask_babel import _
from flask import current_app



def translate(text, target_language):
 
    
    IAM_TOKEN = response.json()['iamToken']
    folder_id = ''
    texts = text
    target_language = 'en'

    body = {
    "targetLanguageCode": target_language,
    "texts": texts,
    "folderId": folder_id,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(IAM_TOKEN)
    }

    response = requests.post('***REMOVED***',
        json = body,
        headers = headers
    )

    if response.status_code != 200:
        return _('Error: the translation service failed.')
    return response.json()['translations'][0]['text']

      
   


