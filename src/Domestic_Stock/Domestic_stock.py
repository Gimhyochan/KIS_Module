from KIS_Constants import Real_Domain, Test_Domain
from KIS_Credentials import KIS, hashkey
import time
import requests
import logging
import json

logger = logging.getLogger(__name__)
class DomesticStock:
    def __init__(self):
        self.headers = {
        "content-type":"application/json",
        "authorization": f"Bearer {KIS.token}",
        "appKey": KIS.appkey,
        "appSecret": KIS.appsecret,
        "tr_id": "",
        "custtype": "P"
        }


def inquire_price(MRKT:str, ISCD:str)-> dict:
    ds = DomesticStock()
    headers = ds.headers
    headers['tr_id'] = "FHKST01010100"
    params = {
        "FID_COND_MRKT_DIV_CODE":MRKT,
        "FID_INPUT_ISCD":ISCD
    }
    headers['hashkey'] = hashkey(params)
    res = requests.get(f"{Real_Domain}/uapi/domestic-stock/v1/quotations/inquire-price", headers=headers, params=params)
    return res.json()
def inquire_ccnl(MRKT:str, ISCD:str)-> dict:
    ds = DomesticStock()
    headers = ds.headers
    headers['tr_id'] = "FHKST01010300"
    params = {
        "FID_COND_MRKT_DIV_CODE":MRKT,
        "FID_INPUT_ISCD":ISCD
    }
    headers['hashkey'] = hashkey(params)
    res = requests.get(f"{Real_Domain}/uapi/domestic-stock/v1/quotations/inquire-ccnl", headers=headers, params=params)
    return res.json()
def inquire_daily_price(MRKT:str, ISCD:str, PERIOD:str= "D", ORG_ADJ:str="0"):
    ds = DomesticStock()
    headers = ds.headers
    headers['tr_id'] = 'FHKST01010400'
    params = {
        "FID_COND_MRKT_DIV_CODE": MRKT,
        "FID_INPUT_ISCD": ISCD,
        "FID_PERIOD_DIV_CODE": PERIOD,
        "FID_ORG_ADJ_PRC": ORG_ADJ
    }
    headers['hashkey'] = hashkey(params)
    res = requests.get(f"{Real_Domain}/uapi/domestic-stock/v1/quotations/inquire-daily-price", headers=headers, params=params)
    return res.json()
def inquire_asking_price_exp_ccn(MRKT:str, ISCD:str):
    ds = DomesticStock()
    headers = ds.headers
    headers['tr_id'] = 'FHKST01010200'
    params = {
        "FID_COND_MRKT_DIV_CODE": MRKT,
        "FID_INPUT_ISCD": ISCD
    }
    headers['hashkey'] = hashkey(params)
    res = requests.get(f"{Real_Domain}/uapi/domestic-stock/v1/quotations/inquire-asking-price-exp-ccn", headers=headers, params=params)
    return res.json()

def inquire_investor(MRKT:str, ISCD:str):
    ds = DomesticStock()
    headers = ds.headers
    headers['tr_id'] = 'FHKST01010900'
    params = {
        "FID_COND_MRKT_DIV_CODE": MRKT,
        "FID_INPUT_ISCD": ISCD
    }
    headers['hashkey'] = hashkey(params)
    res = requests.get(f"{Real_Domain}/uapi/domestic-stock/v1/quotations/inquire-investor", headers=headers, params=params)
    return res.json()

def inquire_member(MRKT:str, ISCD:str):
    ds = DomesticStock()
    headers = ds.headers
    headers['tr_id'] = 'FHKST01010600'
    params = {
        "FID_COND_MRKT_DIV_CODE": MRKT,
        "FID_INPUT_ISCD": ISCD
    }
    headers['hashkey'] = hashkey(params)
    res = requests.get(f"{Real_Domain}/uapi/domestic-stock/v1/quotations/inquire-member", headers=headers, params=params)
    return res.json()

def inquire_elw_price(MRKT:str, ISCD:str):
    """
    MRKT = "W"
    """
    ds = DomesticStock()
    headers = ds.headers
    headers['tr_id'] = 'FHKEW15010000'
    params = {
        "FID_COND_MRKT_DIV_CODE": MRKT,
        "FID_INPUT_ISCD": ISCD
    }
    headers['hashkey'] = hashkey(params)
    res = requests.get(f"{Real_Domain}/uapi/domestic-stock/v1/quotations/inquire-elw-price", headers=headers, params=params)
    return res.json()


