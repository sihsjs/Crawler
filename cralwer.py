import requests

from bs4 import BeautifulSoup as bs
import json
import pandas as pd

url = "http://marketdata1.krx.co.kr/contents/COM/GenerateOTP.jspx"

querystring = {"bld":"MKD/01/0112/01120200/mkd01120200","name":"form"}

headers = {
    'accept': "application/json, text/javascript, */*; q=0.01",
    'accept-encoding': "gzip, deflate",
    'cache-control': "no-cache",
    'postman-token': "abc83be5-3f80-002d-304c-e99e7d54270e"
    }

response_code = requests.request("POST", url, headers=headers, params=querystring)

url = "http://marketdata1.krx.co.kr/contents/SRT/99/SRT99000001.jspx"

querystring = {"pagePath":"/contents/MKD/01/0112/01120200/MKD01120200.jsp"
               ,"code": response_code.text
               ,"isu_cdnm":"전체'","mkt_tp_cd":"0","fr_work_dt":"20160714","to_work_dt":"20160721"}

headers = {
    'accept': "application/json, text/javascript, */*; q=0.01",
    'accept-encoding': "gzip, deflate",
    'cache-control': "no-cache",
    'postman-token': "75dbeaaf-c17d-5d61-1e8a-fcd4e9d6b72e"
    }

response = requests.request("POST", url, headers=headers, params=querystring)

parser_json= json.loads(response.text)

parser = pd.DataFrame(parser_json['result'])
rename_parser = parser.rename(columns={'isu_nm': 'stk_nm_kor', 'trd_dd':'date','all_shrs':'stk_cnt','all_val':'trd_amt'
                                      ,'all_vol':'trd_qty','bal_qty':'bal_short_qty','bal_qtyval':'bal_short_trd_amt'})

output_name = 'short_sell.xlsx'
rename_parser.to_excel(output_name)