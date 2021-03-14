import requests
import json


def get_OAuth2_token(keycloak, client_id, client_secret):
    payload = f'grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}'
    headers = {'content-type': "application/x-www-form-urlencoded"}
    response = requests.request("POST", keycloak, data=payload, headers=headers)
    response_text = json.loads(response.text)
    access_token = response_text['access_token']
    return access_token


def get_token_headers(keycloak, client_id, client_secret):
    token = get_OAuth2_token(keycloak, client_id, client_secret)
    token_headers = {
        'Content-Type': 'application/json',
        "Authorization": "Bearer " + token
    }
    return token_headers


if __name__ == '__main__':
    print(get_token_headers(keycloak='http://192.168.101.126/auth/realms/master/protocol/openid-connect/token',
                            client_id='zqa',
                            client_secret='a043413f-711d-4bd5-9fe5-4ffe3d525fe1'))
