from datetime import datetime

import requests

from DBTables.GDPTable import GDP
from sqlalchemy_globals import postgres_session


def get_year_list():
    current_year = datetime.now().year

    # Since The GDP data is maintained upto 1960 by world bank
    return range(1960, current_year)


def get_gdp_data_of_country(country_iso_code: str) -> dict:
    WORLDBANK_API = f"http://api.worldbank.org/v2/country/{country_iso_code}/indicator/NY.GDP.MKTP.CD?date="  # YEAR to be appended later

    year_gdp_dict = dict()

    year_list = get_year_list()
    for year in year_list:
        print(f"{country_iso_code} : {year_gdp_dict}")
        response = requests.get(WORLDBANK_API + str(year) + "&format=json")  # To get json response for respective year
        year_gdp_dict[year] = response.json()[1][0]['value']

    return {country_iso_code: year_gdp_dict}


# 2 character iso codes of various countries
INDIA_ISO_CODE = "in"
US_ISO_CODE = "us"
CHINA_ISO_CODE = "cn"

india_gdp_data = get_gdp_data_of_country(INDIA_ISO_CODE)
us_gdp_data = get_gdp_data_of_country(US_ISO_CODE)
china_gdp_data = get_gdp_data_of_country(CHINA_ISO_CODE)

all_gdp_data = dict()
all_gdp_data.update(india_gdp_data)
all_gdp_data.update(us_gdp_data)
all_gdp_data.update(china_gdp_data)

# Populate the GDP in the tables

for country, gdp_data in all_gdp_data.items():
    for year, gdp in gdp_data.items():
        gdp_obj = GDP(country = country, year = year, gdp = gdp)
        postgres_session.add(gdp_obj)
        postgres_session.commit()
