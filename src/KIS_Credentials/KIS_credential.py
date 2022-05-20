import requests
import os
import logging
import json
import time
from KIS_Constants import Real_Domain, Test_Domain

logger = logging.getLogger(__name__)
class KIS:
    def __init__(self):
        if not  os.path.exists(os.path.expanduser('~')+"/.KIS"):
            logger.warning("Create folder ~/.KIS/")
            os.makedirs(os.path.expanduser('~')+"/.KIS")
        self.token = ""
        self.appkey=""
        self.appsecret=""
        self._config()
    def auth(self):
        logger.warning("Regenerate Access Token")
        headers = {"content-type":"application/json"}
        data = {
            "grant_type":"client_credentials",
            "appkey":self.appkey, 
            "appsecret":self.appsecret
        }
        res = requests.post(Real_Domain+"/oauth2/tokenP", headers=headers, data=json.dumps(data))
        self.token = json.loads(res.text)['access_token']
        f_credential = open(os.path.expanduser('~') + "/.KIS/credential", "w")
        f_credential.write(json.dumps({
            "appkey": self.appkey,
            "appsecret": self.appsecret,
            "token": self.token,
            "token_expire": int(time.time()) + int(json.loads(res.text)['expires_in']) - ( 60 * 60)
        }))
    def _register(self):
        self.appkey = input("App Key: ")
        self.appsecret = input("App Secret: ")
        logger.warning(f"Confimation\nappkey: \"{self.appkey}\"\nappsecret: \"{self.appsecret}\"")

    def _config(self):
        logger.warning("Use this on TRUSTED DEVICE")
        try:
            f_credential = open(os.path.expanduser('~') + "/.KIS/credential", "r")
            credential = json.loads(f_credential.read())
            f_credential.close()
        except:
            credential = {}
        self.appkey = credential.get('appkey', None)
        self.appsecret = credential.get('appsecret', None)
        if self.appkey==None or self.appsecret==None:
            self._register()
        self.token = credential.get('token', "")
        self.token_expire = credential.get('token_expire', int(time.time())) # get approximate estimated expire time
        if self.token_expire <= int(time.time()):
            self.auth()
        else:
            f_credential = open(os.path.expanduser('~') + "/.KIS/credential", "w")
            f_credential.write(json.dumps(
                {
                    "appkey": self.appkey,
                    "appsecret": self.appsecret,
                    "token": self.token,
                    "token_expire": self.token_expire
                }
            )
            )

    def hashkey(self, body: dict):
        headers = {
            "content-type":"application/json",
            "appkey": self.appkey,
            "appsecret": self.appsecret
        }
        data = body
        res = requests.post(Real_Domain+"/uapi/hashkey", headers=headers, data=json.dumps(data))
        return json.loads(res.text)["HASH"]
