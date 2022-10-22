"""global configure arguments"""
from Ingram.utils.base import singleton
from Ingram.utils.net import get_user_agent


@singleton
class Config:

    def __init__(self):
        self.TIMEOUT = 3  # (default) will be reset in the run_ingram.py
        self.USERS = ['admin']  # user names for Brute force cracking of weak passwords
        self.PASSWDS = ['a1234567', 'A1234567', 'abcd1234', 'Abcd1234', 'Admin123', 'admin123', 'hd543211', 'Admin12345', 'admin12345', '12345', '123456', 'Hd543211', 'admin123456', 'Admin123456', 'abc123abc', 'Abcd12345', 'abcd12345', 'asdf1234', 'abc12345', '12345admin', '12345abc', 'abc123abc', '123abc123']
        self.USERAGENT = get_user_agent()  # to save time, we only get user agent once.
        self.PORT = [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 180, 280, 380, 480, 580, 680, 780, 880, 980, 1080, 8888, 8000, 8001, 8002, 8003, 8004, 8005, 8008, 8080, 8081, 8085, 8086, 8088, 8181, 9000, 37777, 34599, 34582]

        # device names
        self.NON_MATCH_DEV = 'other'
        self.HIKVISION = 'hikvision'
        self.DAHUA = 'dahua'
        self.UNIVIEW_NVR = 'uniview-nvr'
        self.DLINK_DCS = 'dlink-dcs'
        self.CCTV = 'cctv'
        self.DVR = 'dvr'  # cve-2018-9995
        self.TENDA_W15E = 'tenda-w15e'
        self.TPLINK = 'tplink'
        self.HUAWEI = 'huawei'


global config
config = Config()
