def _get_currency(resource, transform=(lambda x: x)):
    data={
        'items':[
            {'code': 'usd', 'amount_to_usd': 1.00},
            {'code': 'eur', 'amount_to_usd': 1.40},
            {'code': 'yen', 'amount_to_usd': 1.50},
            {'code': 'inr', 'amount_to_usd': 0.70}
        ]
    }

    my_resource = data[resource]
    # return list(map(transform, my_resource))
    return [transform(x) for x in my_resource]

def get_currency_codes():
    return _get_currency('items', lambda x: x['code'].upper())

print(get_currency_codes())