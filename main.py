import os
import requests

from variables import Polygon as p126
from polygon_token import get_token_headers
from payloads import correct_start_time, correct_code, get_payload

collection=[]
path_to_json = 'requests_bodies/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
for json_file in json_files:
    collection.append(path_to_json+json_file)


class ZqaAnalysisRequestsSimple:
    def post_new(self):
        endpoint = f'{p126.IP}{p126.service_port}{p126.service_url}'
        print()
        print(f'endpoint = {endpoint}')
        for file in collection:
            try:
                code = file.split('/')[1].split('.')[0]
                correct_code(file, code)
                correct_start_time(file)
                payload = get_payload(file)
                headers = get_token_headers(p126.TOKEN_URL, p126.AUTH_CLIENT_ID, p126.AUTH_CLIENT_SECRET)
                response = requests.post(url=endpoint, headers=headers, data=payload)
                print()
                print(f'{code} = {response.status_code}')
                assert response.status_code == 200
            except AssertionError:
                pass


if __name__ == '__main__':
    print(collection)
    ZqaAnalysisRequestsSimple().post_new()
