from exchange.models import ProviderValues
from exchange.providers.provider import provider_list
from django.utils.module_loading import import_string
from django.http import JsonResponse

# Create your views here.


def get_currencies_view(request):
    usd_currencies = {}
    eur_currencies = {}
    gbp_currencies = {}
    for provider in provider_list:
        adapter_class = import_string(provider)
        adapter = adapter_class()
        response = adapter.get_currencies()
        clean_response = adapter.clean_response(response)
        usd_currencies[adapter.provider_name] = clean_response['USD']
        eur_currencies[adapter.provider_name] = clean_response['EUR']
        gbp_currencies[adapter.provider_name] = clean_response['GBP']
        provider_value = ProviderValues()
        provider_value.provider_name = adapter.provider_name
        provider_value.usd = clean_response['USD']
        provider_value.eur = clean_response['EUR']
        provider_value.gbp = clean_response['GBP']
        provider_value.save()
    usd_provider_list = sorted(usd_currencies.items(), key=lambda x: x[1])
    eur_provider_list = sorted(eur_currencies.items(), key=lambda x: x[1])
    gbp_provider_list = sorted(gbp_currencies.items(), key=lambda x: x[1])

    cheapest_usd_provider, cheapest_usd_value = usd_provider_list[0]
    cheapest_eur_provider, cheapest_eur_value = eur_provider_list[0]
    cheapest_gbp_provider, cheapest_gbp_value = gbp_provider_list[0]

    response = {
        "USD": {
            cheapest_usd_provider: cheapest_usd_value
        },
        "EUR": {
            cheapest_eur_provider: cheapest_eur_value
        },
        "GBP": {
            cheapest_gbp_provider: cheapest_gbp_value
        }
    }
    return JsonResponse(response)


