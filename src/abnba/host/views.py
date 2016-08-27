import json

import django.views.generic
import django.http

import requests

def get_auth_token():
    data = {
        'grant_type': 'password',
        'password': 'bankowy27',
        'username': 'pawlowska.magdalena@gmail.com',
        'client_id': '3092nxybyb0otqw18e8nh5nty',
    }
    r = requests.post('https://api.airbnb.com/v1/authorize', data=data)
    data = json.loads(r.text)
    print data
    return data['access_token']


class AuthView(django.views.generic.View):

    def get(self, request, *args, **kwargs):
        headers = {
            'X-Airbnb-OAuth-Token': get_auth_token(),
        }
        data = {
            'role': 'host',
            '_format': 'for_mobile_inbox',
            '_offset': '10',
            'selected_inbox_type': 'host',
            'currency': 'PLN',
            'locale': 'pl',
        }
        r = requests.get('https://api.airbnb.com/v2/threads', headers=headers, params=data)
        return django.http.HttpResponse(r.text)



