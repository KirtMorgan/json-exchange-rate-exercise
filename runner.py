from exchange_oop_json import RatesParser

rates_obj = RatesParser("json_2.json")
print(rates_obj)
for key in rates_obj.rates:
    print(key, rates_obj.rates[key])
