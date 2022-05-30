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

api_key = os.environ['TOKEN']

today = dt.datetime.date(dt.datetime.now())


def get_detail_by_period(token, date_from, date_to):
    url = 'https://suppliers-stats.wildberries.ru/api/v1/supplier/reportDetailByPeriod'
    params = {
        'key': token,
        'dateFrom': date_from,
        'dateto': date_to,
        'limit': 10000,
        'rrdid': 0
    }
    response = requests.get(url, params=params)
    with open(f'{today}.json', 'w') as f:
        json.dump(response.json(), f, indent=2, ensure_ascii=False)
    return f'{today}.json'


def get_FBO(json_file, barcode):
    count = 0
    index = 0
    with open(json_file) as f:
        templates = json.load(f)
    for card in templates:

        if card['office_name'] != "Склад поставщика" and card['supplier_oper_name'] == 'Продажа':
            count += 1

    print("Продаж FBO: ", count)
    return


#get_detail_by_period(api_key, date_from = '2022-05-18', date_to = '2022-05-18')

get_FBO(json_file=f"{today}.json", barcode='2008082456003')
