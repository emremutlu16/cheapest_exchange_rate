import requests
from urllib.parse import urljoin


class BaseAdapter:
    provider_name = 'provider'
    base_url = ''
    endpoint = ''

    def get_currencies(self):
        response = requests.get(urljoin(self.base_url, self.endpoint))
        if not response.status_code == 200:
            raise Exception(response.text)
        return response.json()

    def clean_response(self, response):
        data = response['data']
        result_dict = {}
        for d in data:
            result_dict[d['symbol'][:3].upper()] = d['amount']
        return result_dict
