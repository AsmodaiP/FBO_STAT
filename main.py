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

date_from = '2022-05-01'
date_to = '2022-05-02'


class OrderFBO(NamedTuple):
    realizationreport_id: int
    suppliercontract_code: None
    rrd_id: int
    gi_id: int
    subject_name: str
    nm_id: int
    brand_name: str
    sa_name: str
    ts_name: str
    barcode: str
    doc_type_name: str
    quantity: int
    retail_price: float
    retail_amount: float
    sale_percent: float
    commission_percent: float
    office_name: str
    supplier_oper_name: str
    order_dt: str
    sale_dt: str
    rr_dt: str
    shk_id: int
    retail_price_withdisc_rub: float
    delivery_amount: int
    return_amount: int
    delivery_rub: float
    gi_box_type_name: str
    product_discount_for_report: float
    supplier_promo: int
    rid: int
    ppvz_spp_prc: float
    ppvz_kvw_prc_base: float
    ppvz_kvw_prc: float
    ppvz_sales_commission: float
    ppvz_for_pay: float
    ppvz_reward: float
    ppvz_vw: float
    ppvz_vw_nds: float
    ppvz_office_id: int
    ppvz_office_name: str
    ppvz_supplier_id: int
    ppvz_supplier_name: str
    ppvz_inn: str
    declaration_number: str
    sticker_id: str
    bonus_type_name: str



def get_detail_by_period(token, date_from, date_to) -> List[OrderFBO]:
    url = 'https://suppliers-stats.wildberries.ru/api/v1/supplier/reportDetailByPeriod'
    params={
        'key': token,
        'dateFrom': date_from,
        'dateto': date_to,
        'limit': 10,
        'rrdid': 0
    }
    response = requests.get(url, params=params)
    print(response.text)
    return [OrderFBO(**order) for order in response.json()]


get_detail_by_period(token, '2022-04-19', '2023-12-31')
