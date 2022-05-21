import requests
import os
import logging
import json
import time
from KIS_Constants import Real_Domain, Test_Domain

logger = logging.getLogger(__name__)
class KIS:
    appkey = ""
    appsecret = ""
    token = ""
    token_expire = -1
    def __init__(self):
        if not  os.path.exists(os.path.expanduser('~')+"/.KIS"):
            logger.warning("Create folder ~/.KIS/")
            os.makedirs(os.path.expanduser('~')+"/.KIS")
        self._config()
    def auth(self):
        logger.warning("Regenerate Access Token")
        headers = {"content-type":"application/json"}
        data = {
            "grant_type":"client_credentials",
            "appkey":KIS.appkey, 
            "appsecret":KIS.appsecret
        }
        res = requests.post(f"{Real_Domain}/oauth2/tokenP", headers=headers, data=json.dumps(data))
        KIS.token = json.loads(res.text)['access_token']
        KIS.token_expire = int(time.time()) + int(json.loads(res.text)['expires_in']) - ( 60 * 60)
        f_credential = open(os.path.expanduser('~') + "/.KIS/credential", "w")
        f_credential.write(json.dumps({
            "appkey": KIS.appkey,
            "appsecret": KIS.appsecret,
            "token": KIS.token,
            "token_expire": KIS.token_expire
        }))
    def _register(self):
        KIS.appkey = input("App Key: ")
        KIS.appsecret = input("App Secret: ")
        logger.warning(f"Confimation\nappkey: \"{KIS.appkey}\"\nappsecret: \"{KIS.appsecret}\"")

    def _config(self):
        logger.warning("Use this on TRUSTED DEVICE")
        try:
            f_credential = open(os.path.expanduser('~') + "/.KIS/credential", "r")
            credential = json.loads(f_credential.read())
            f_credential.close()
        except:
            credential = {}
        KIS.appkey = credential.get('appkey', None)
        KIS.appsecret = credential.get('appsecret', None)
        if KIS.appkey==None or KIS.appsecret==None:
            self._register()
        KIS.token = credential.get('token', "")
        KIS.token_expire = credential.get('token_expire', int(time.time())) # get approximate estimated expire time
        if KIS.token_expire <= int(time.time()):
            self.auth()
        else:
            f_credential = open(os.path.expanduser('~') + "/.KIS/credential", "w")
            f_credential.write(json.dumps(
                {
                    "appkey": KIS.appkey,
                    "appsecret": KIS.appsecret,
                    "token": KIS.token,
                    "token_expire": KIS.token_expire
                }
            )
            )

def hashkey(body: dict):
    headers = {
        "content-type":"application/json",
        "appkey": KIS.appkey,
        "appsecret": KIS.appsecret
    }
    data = body
    res = requests.post(f"{Real_Domain}/uapi/hashkey", headers=headers, data=json.dumps(data))
    return json.loads(res.text)["HASH"]
