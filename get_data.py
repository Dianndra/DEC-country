import pandas as pd
import requests


def get_country_data():
    url = 'https://restcountries.com/v3.1/all?fields=name,independent,unMember,startOfWeek,currencies,region,subregion,languages,area,idd,capital,population,continents'

    try:
        response = requests.get(url)
        response.raise_for_status()

        country_list = []
        country_data = response.json()

        for country in country_data:
            # get native name
            native_name = country['name'].get('nativeName', {})
            common_name = [lang_name['common'] for lang_name in native_name.values()] 
            common_native_name = ', '.join(common_name)

            # get languages
            lang = country.get('languages', {})
            languages = ', '.join(list(lang.values()))

            # get currency code, name, symbol
            curr = country.get('currencies', {})

            currency_code = list(curr.keys()) 
            currency_code = ', '.join(currency_code)

            currency_name = [currency['name'] for currency in curr.values()] 
            currency_name = ', '.join(currency_name)

            currency_symbol = [currency['symbol'] for currency in curr.values()] 
            currency_symbol = ', '.join(currency_symbol)

            # get capital
            cap = country.get('capital', 'N/A')
            capital = ', '.join(cap)

            # get continent
            con = country.get('continents', 'N/A')
            continent = ', '.join(con)

            # get idd 
            root = country['idd'].get('root', 'N/A')
            suffix = country['idd'].get('suffixes', 'N/A') 
            idd = [root + s for s in suffix]
            idd = ','.join(idd)

            country_list.append({
                'Country_name': country['name']['common'],
                'Independence': country.get('independent', 'N/A'),
                'United_Nation_members': country['unMember'],
                'Start_Of_Week': country['startOfWeek'],
                'Official_country_name': country['name']['official'],
                'Common_native_name': common_native_name,
                'Currency_code': currency_code,
                'Currency_name': currency_name,
                'Currency_symbol': currency_symbol,
                'Idd': idd,
                'Capital': capital,
                'Region': country['region'],
                'Sub_region': country['subregion'],
                'Languages': languages,
                'Area': country['area'],
                'Population': country['population'],
                'Continents': continent
            })

            country_data = pd.DataFrame(country_list)
        return country_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()
    
get_country_data()