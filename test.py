from time import sleep
from typing import NamedTuple, TypedDict, List
from collections import namedtuple
from pyparsing import tokenMap
import requests
from googleapiclient.discovery import build
import logging
import os
import datetime as dt
import json
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

token = os.environ['TOKEN']

date_from = '2022-03-01'
date_to = '2022-05-25'

def get_detail_by_period(token, date_from, date_to):
    url = 'https://suppliers-stats.wildberries.ru/api/v1/supplier/reportDetailByPeriod'
    params={
        'key': token,
        'dateFrom': date_from,
        'dateto': date_to,
        'limit': 300,
        'rrdid': 0
    }
    response = requests.get(url, params=params)
    with open('jsonFBO.txt', 'w') as f:
        json.dump(response.json(), f,  indent=2, ensure_ascii=False)
    return 'jsonFBO.txt'

def get_FBO(json_file_fbo, barcode):
    with open(f'{json_file_fbo}') as f:
        templates = json.load(f)
    for card in templates:
        if card['barcode'] == barcode and card['office_name'] != "Склад поставщика":
            print(card['supplier_oper_name'])


#get_detail_by_period(token, date_from, date_to)

get_FBO('jsonFBO.txt', barcode='2011763633013')
