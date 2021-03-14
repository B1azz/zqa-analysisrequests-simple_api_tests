from datetime import datetime


class Polygon:
    IP = 'http://192.168.101.126'
    service_port = ':9014'
    service_url = '/analysisrequest'
    AUTH_URL = 'http://192.168.101.126/auth/realms/master/protocol/openid-connect/auth'
    TOKEN_URL = 'http://192.168.101.126/auth/realms/master/protocol/openid-connect/token'
    FLOW = 'authorizationCode'
    AUTH_CLIENT_ID = 'zqa'
    AUTH_CLIENT_SECRET = 'a043413f-711d-4bd5-9fe5-4ffe3d525fe1'
    TOKEN_HEADERS = {
        'Content-Type': 'application/json',
        'User-Agent': 'PostmanRuntime/7.26.10',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }


class Uuid:
    time_now = str(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
    # Соляная кислота
    material = '2c40b220-0df8-11eb-aadc-5b9496d19ca3'
    # методикаОпределения1
    sample_template = '0e0238fd-7de8-4125-8568-d4bd85b9eeb0'
    # Испытательная лаборатория
    subdivision = 'b9bf5590-1f49-11eb-8925-5984a0cb98e0'
    # Цех обогащения
    sampling_point = '3c0ab790-1f42-11eb-b988-233c1c583b3b'
    # Без маски
    sample_log = 'ac2646e1-da3d-423f-9eab-28d222ee159d'
    # admin
    performer = 'c64bf64f-74e9-4ac6-9299-195de10413b2'
