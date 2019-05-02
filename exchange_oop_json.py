import json


class RatesParser:

    def __init__(self, rate_file):

        rates_info_dict = self.__open_json_file(rate_file)
        self.base = rates_info_dict['base']
        self.date = rates_info_dict['date']
        self.rates = rates_info_dict['rates']
        self.aud = self.rates['AUD']
        self.gbp = self.rates['GBP']

    def __open_json_file(self, file_name_path):
        with open(file_name_path) as rates:
            return json.load(rates)
