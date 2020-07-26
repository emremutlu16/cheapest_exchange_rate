from exchange.core.base_adapter import BaseAdapter


class Provider2Adapter(BaseAdapter):
    provider_name = 'provider2'
    base_url = 'https://run.mocky.io/v3/'
    endpoint = 'cff2fa19-a599-46c7-a83c-c891ba721561'

    def clean_response(self, response):
        data = response['result']
        result_dict = {}
        for d in data:
            result_dict[d['from'].upper()] = d['value']
        return result_dict
