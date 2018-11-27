import allatok
import pandas as pd
from config import config

import requests

def add(x, y):
	return x + y

def get_holidays(country, year):
	params = {
		'country' : country,
		'year': year,
		'key': config.holiday_api_key
	}	
	response = requests.get(
		'https://holidayapi.com/v1/holidays',
		params=params
		)
	r = response.json()

	return r



if __name__ == '__main__':

	print(get_holidays(country='HU', year=2017))
    # print(add(3,5))
    # allatok.kutya()

    # s = pd.Series([1,2,3,5,6])

    # print(s)

    # print(config.secret)